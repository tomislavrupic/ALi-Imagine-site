#!/usr/bin/env python3
"""Build the portable skill and checksum together from the app source."""
import hashlib,pathlib,sys,zipfile
source=pathlib.Path(sys.argv[1]).resolve()/'mcp-server/ali-resolve'
root=pathlib.Path(__file__).resolve().parents[1]
target=root/'downloads/ali-resolve-skill-1.1.0.zip'
files=['SKILL.md','README.md','scripts/shot.py','scripts/mcp.py','scripts/mcp_shot.py','scripts/test_mcp_shot.py']
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED) as archive:
 for name in files:
  data=(source/name).read_bytes()
  assert b'/Users/thecore' not in data and b'/Volumes/Samsung' not in data
  info=zipfile.ZipInfo('ali-resolve/'+name,(2026,10,7,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16
  archive.writestr(info,data)
target.with_suffix('.zip.sha256').write_text(hashlib.sha256(target.read_bytes()).hexdigest()+'  '+target.name+'\n')
print(target.name)
