#!/usr/bin/env python3
"""MCP submission and verified Resolve placement using frozen one-shot receipts."""
import argparse, importlib.util, json, pathlib, sys
import shot
path=pathlib.Path.home()/'Library/Application Support/ALi-Imagine/mcp/server.py'
spec=importlib.util.spec_from_file_location('ali_mcp',path)
client=importlib.util.module_from_spec(spec);spec.loader.exec_module(client)
call=client.call

def submit(folder,request):
    receipt=folder/'shot.json';data=json.loads(receipt.read_text())
    if data['state']!='prepared':raise RuntimeError('Already submitted or uncertain; reconcile the receipt before retry')
    if request.get('projectId')!=data['payload']['project_id']:raise RuntimeError('ALi project differs from frozen receipt')
    schema=next(t for t in client.TOOLS if t['name']=='ali_generate')['inputSchema']
    client.validate({'request':request},schema)
    for path,sha in data['anchor_hashes'].items():
        if shot.digest(path)!=sha:raise RuntimeError('Captured anchor changed')
    data.update(state='mcp_submission_pending',transport='ali-imagine-mcp',mcp_request=request)
    shot.save(receipt,data)
    job=call('ali_generate',{'request':request})
    data.update(state='mcp_submitted',job_id=job['id']);shot.save(receipt,data)
    return data

def inspect(folder):
    receipt=folder/'shot.json';data=json.loads(receipt.read_text())
    if data.get('transport')!='ali-imagine-mcp' or not data.get('job_id'):raise RuntimeError('No known MCP job; reconcile uncertain submission')
    job=call('ali_inspect_job',{'job_id':data['job_id']})
    data['mcp_job']=job
    if job['project_id']!=data['mcp_request']['projectId']:raise RuntimeError('Job project mismatch')
    if job['request']['providerId']!=data['mcp_request']['providerId']:raise RuntimeError('Job provider mismatch')
    outputs=call('ali_list_outputs',{'project_id':job['project_id']}) if job['state']=='completed' else []
    data['mcp_output']=next((o for o in outputs if o['id']==job.get('output_asset_id') and o['job_id']==job['id']),None)
    shot.save(receipt,data);return data

def place(folder):
    data=inspect(folder);receipt=folder/'shot.json'
    if data.get('placement'):raise RuntimeError('Already placed; reconcile the placement receipt')
    output=data['mcp_output']
    if data['mcp_job']['state']!='completed' or not output or not pathlib.Path(output['path']).is_file():raise RuntimeError('No matching completed local output')
    api=shot.plugin();resolve,project,timeline=shot.resolve()
    if not timeline or project.GetName()!=data['project'] or timeline.GetUniqueId()!=data['timeline_id']:raise RuntimeError('Activate original project/timeline')
    for track in range(1,timeline.GetTrackCount('video')+1):
        for item in timeline.GetItemListInTrack('video',track) or []:
            media=item.GetMediaPoolItem()
            if media and item.GetStart()==data['record_frame'] and media.GetClipProperty('File Path')==output['path']:raise RuntimeError('Output already present; reconcile placement')
    pool=project.GetMediaPool();old=pool.GetCurrentFolder();tc=timeline.GetCurrentTimecode()
    try:
        clip=api.import_output(project,output['path'])
        if not timeline.SetCurrentTimecode(api.frames_to_timecode(data['record_frame'],data['fps'])):raise RuntimeError('Seek failed')
        item=api.place_above_playhead(project,timeline,clip)
        data['placement']={'start':item.GetStart(),'end':item.GetEnd(),'path':output['path']};shot.save(receipt,data)
        if item.GetStart()!=data['record_frame']:raise RuntimeError('Unexpected placement; inspect receipt before retry')
        if not resolve.GetProjectManager().SaveProject():raise RuntimeError('Placed but save failed; do not place again')
    finally:timeline.SetCurrentTimecode(tc);pool.SetCurrentFolder(old)
    return data

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('action',choices=['submit','poll','place']);parser.add_argument('directory');parser.add_argument('--request-file');args=parser.parse_args();folder=pathlib.Path(args.directory).resolve()
    try:
        if args.action=='submit':
            if not args.request_file:parser.error('--request-file required')
            result=submit(folder,json.loads(pathlib.Path(args.request_file).read_text()))
        elif args.action=='poll':result=inspect(folder)
        else:result=place(folder)
        print(json.dumps(result,indent=2))
    except Exception as e:print(str(e),file=sys.stderr);sys.exit(1)
