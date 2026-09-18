#!/usr/bin/env python3
"""One-shot receipts around the installed ALi Resolve bridge. No UI launch."""
import argparse, hashlib, importlib.util, json, shutil, sys
from pathlib import Path

def plugin():
    path=Path.home()/'Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/ALi Resolve/ali_resolve.py'
    spec=importlib.util.spec_from_file_location('ali_panel',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def resolve():
    sys.path.insert(0,'/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
    import DaVinciResolveScript as d
    r=d.scriptapp('Resolve')
    if not r: raise RuntimeError('Resolve scripting connection unavailable')
    p=r.GetProjectManager().GetCurrentProject();t=p.GetCurrentTimeline() if p else None
    if not t: raise RuntimeError('Open a project and timeline')
    return r,p,t

def save(path,data):
    temp=path.with_suffix('.tmp');temp.write_text(json.dumps(data,indent=2));temp.replace(path)

def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['status','prepare','submit','poll','place'])
    parser.add_argument('directory',nargs='?')
    parser.add_argument('--mode',choices=['start_frame','first_last','lip_sync','text_only'],default='start_frame')
    parser.add_argument('--prompt-file');parser.add_argument('--duration',type=int,choices=[5,10,20],default=5)
    parser.add_argument('--quality',choices=['preview','working','final'],default='preview')
    a=parser.parse_args();api=plugin()
    if a.action=='status':
        _,p,t=resolve()
        print(json.dumps({'ali':api.api('GET','/status'),'resolve':{'project':p.GetName(),'timeline':t.GetName(),'timeline_id':t.GetUniqueId(),'timecode':t.GetCurrentTimecode(),'fps':t.GetSetting('timelineFrameRate'),'marks':t.GetMarkInOut()}},indent=2));return
    if not a.directory: parser.error('directory required')
    folder=Path(a.directory).resolve();receipt=folder/'shot.json'
    if a.action=='prepare':
        if receipt.exists(): raise RuntimeError('Receipt exists; use a new take directory')
        if not a.prompt_file: parser.error('--prompt-file required')
        prompt=Path(a.prompt_file).read_text().strip()
        if not prompt: raise RuntimeError('Empty prompt')
        if a.duration>{'preview':20,'working':10,'final':5}[a.quality]: raise RuntimeError('Duration exceeds quality preset')
        _,p,t=resolve();fps=api.timeline_fps(p,t)
        if fps!=round(fps): raise RuntimeError('Fractional fps needs verified timecode conversion')
        status=api.api('GET','/status');tc=t.GetCurrentTimecode();marks=t.GetMarkInOut() or {}
        record=api.timecode_to_frames(tc,fps);frames=[];audio=None
        folder.mkdir(parents=True,exist_ok=True)
        if a.mode=='first_last':
            frames=api.capture_in_out(p,t)
            mark=(marks.get('video') or marks.get('all'))['in'];base=t.GetStartFrame()
            record=int(mark) if int(mark)>=base else base+int(mark)
        elif a.mode=='lip_sync':
            frame,audio=api.capture_frame_and_audio(p,t);frames=[frame]
        elif a.mode=='start_frame': frames=[api.capture_current(p,'skill')]
        anchors=[]
        for i,frame in enumerate(frames):
            dest=folder/f'anchor-{i+1}.png';shutil.copy2(frame,dest);anchors.append(str(dest))
        payload=api.build_job_payload(prompt,api.MODE_VALUES.index(a.mode),anchors,[],audio,api.DURATION_VALUES.index(a.duration),api.QUALITY_VALUES.index(a.quality))
        payload['project_id']=status['project_id']
        data={'project':p.GetName(),'timeline':t.GetName(),'timeline_id':t.GetUniqueId(),'record_frame':record,'fps':fps,'captured_timecode':tc,'marks':marks,'anchor_hashes':{x:digest(x) for x in anchors},'payload':payload,'state':'prepared'}
        save(receipt,data)
    else:
        data=json.loads(receipt.read_text())
        if a.action=='submit':
            if data['state']!='prepared': raise RuntimeError('Already submitted or uncertain; reconcile receipt instead of retrying')
            status=api.api('GET','/status')
            if not status.get('ready') or status.get('busy') or status.get('active_job_id'): raise RuntimeError('Engine unavailable or another job active')
            if status['project_id']!=data['payload']['project_id']: raise RuntimeError('ALi project changed')
            for path,sha in data['anchor_hashes'].items():
                if digest(path)!=sha: raise RuntimeError('Anchor changed')
            data['state']='submission_pending';save(receipt,data)
            job=api.api('POST','/jobs',data['payload'],timeout=30)
            data.update(state='submitted',job_id=job['id']);save(receipt,data)
        elif a.action=='poll':
            if not data.get('job_id'): raise RuntimeError('No known job ID; reconcile uncertain submission')
            result=api.api('GET','/jobs/'+data['job_id'])
            data['result']=result;save(receipt,data)
        elif a.action=='place':
            if data.get('placement'): raise RuntimeError('Already placed; receipt contains timeline coordinates')
            if not data.get('job_id'): raise RuntimeError('No submitted job')
            result=api.api('GET','/jobs/'+data['job_id'])
            output=result.get('output');job=result.get('job',{})
            if job.get('state')!='completed' or not output or not Path(output['path']).is_file(): raise RuntimeError('Matching job has no completed local output')
            r,p,t=resolve()
            if p.GetName()!=data['project'] or t.GetUniqueId()!=data['timeline_id']: raise RuntimeError('Activate the original target project/timeline')
            for tr in range(1,t.GetTrackCount('video')+1):
                for item in t.GetItemListInTrack('video',tr) or []:
                    media=item.GetMediaPoolItem()
                    if media and item.GetStart()==data['record_frame'] and media.GetClipProperty('File Path')==output['path']: raise RuntimeError('Result already present; reconcile placement receipt')
            mp=p.GetMediaPool();old=mp.GetCurrentFolder();tc=t.GetCurrentTimecode()
            try:
                clip=api.import_output(p,output['path'])
                if not t.SetCurrentTimecode(api.frames_to_timecode(data['record_frame'],data['fps'])): raise RuntimeError('Seek failed')
                item=api.place_above_playhead(p,t,clip)
                if item.GetStart()!=data['record_frame']: raise RuntimeError('Unexpected placement; inspect before retry')
                data['placement']={'start':item.GetStart(),'end':item.GetEnd(),'path':output['path']};save(receipt,data)
                if not r.GetProjectManager().SaveProject(): raise RuntimeError('Placement made but save failed')
            finally: t.SetCurrentTimecode(tc);mp.SetCurrentFolder(old)
    print(json.dumps(data,indent=2))

if __name__=='__main__':
    try: main()
    except Exception as error:
        print(str(error),file=sys.stderr);sys.exit(1)
