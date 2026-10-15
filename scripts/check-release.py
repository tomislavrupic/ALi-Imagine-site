#!/usr/bin/env python3
import hashlib,json,pathlib,re,zipfile
from html.parser import HTMLParser
root=pathlib.Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text();feed=json.loads((root/'updates/latest.json').read_text())
version=feed['version'];assert f'/v{version}/ALi-Imagine_{version}_aarch64.dmg' in html
assert feed['platforms']['darwin-aarch64']['url'].endswith((f'/v{version}/ALi-Imagine.app.tar.gz', f'/v{version}/ALi-Imagine_{version}_updater-r2.app.tar.gz'))
assert len(feed['platforms']['darwin-aarch64']['signature'])>100
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if key in ('src','href') and value and not value.startswith(('https:','http:','#','data:','mailto:')):
    assert (root/value.split('?')[0]).is_file(),value
Links().feed(html)
skill_paths=set(re.findall(r'downloads/ali-resolve-skill-[0-9.]+\.zip(?![.])',html))
assert len(skill_paths)==1,skill_paths
p=root/skill_paths.pop();expected=p.with_suffix('.zip.sha256').read_text().split()[0]
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
allowed={'ali-resolve/SKILL.md','ali-resolve/README.md','ali-resolve/scripts/shot.py','ali-resolve/scripts/mcp.py','ali-resolve/scripts/mcp_shot.py','ali-resolve/scripts/test_mcp_shot.py','ali-resolve/references/flux3.md','ali-resolve/references/flux3-prompting.md'}
with zipfile.ZipFile(p) as archive:
 assert set(archive.namelist())==allowed
 for name in allowed:
  data=archive.read(name)
  assert not any(s in data for s in (b'/Users/thecore',b'/Volumes/Samsung',b'-----BEGIN PRIVATE KEY'))
assert '17843' in (root/'downloads/ali-resolve-setup.txt').read_text()
assert 'authorization-gated' in html
print(f'Release {version}: download/feed consistency, local links, skill allowlist and checksum pass.')
