#!/usr/bin/env python3
"""Build the portable skill and checksum together from the app source."""
import argparse,hashlib,pathlib,re,zipfile
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('app_source',type=pathlib.Path)
parser.add_argument('--output-dir',type=pathlib.Path)
args=parser.parse_args()
source=args.app_source.resolve()/'mcp-server/ali-resolve'
root=pathlib.Path(__file__).resolve().parents[1]
version=re.search(r'^# ALi Resolve skill ([0-9]+\.[0-9]+\.[0-9]+)$',(source/'README.md').read_text(),re.MULTILINE)
if not version: raise SystemExit('Missing skill version in README.md')
output_dir=args.output_dir or root/'downloads'
output_dir.mkdir(parents=True,exist_ok=True)
target=output_dir/f'ali-resolve-skill-{version.group(1)}.zip'
files=['SKILL.md','README.md','scripts/shot.py','scripts/mcp.py','scripts/mcp_shot.py','scripts/test_mcp_shot.py','references/flux3.md','references/flux3-prompting.md']
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED) as archive:
 for name in files:
  data=(source/name).read_bytes()
  assert b'/Users/thecore' not in data and b'/Volumes/Samsung' not in data
  info=zipfile.ZipInfo('ali-resolve/'+name,(2026,10,7,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
  archive.writestr(info,data)
target.with_suffix('.zip.sha256').write_text(hashlib.sha256(target.read_bytes()).hexdigest()+'  '+target.name+'\n')
print(target.name)
