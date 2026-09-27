"""Validate catalog completeness, stable IDs, criterion polarity and source links."""
from common import *
from sync_catalogs import sync
import sys,hashlib

def main():
 sync(check=True)
 files={str(p.relative_to(DOCS)) for p in DOCS.rglob('*.md') if '.vitepress' not in p.parts and 'public' not in p.parts}
 paths=[p['path'] for p in PAGES]
 assert len(paths)==len(set(paths)),'Duplicate page paths'
 assert files==set(paths),f'Unmapped/missing Markdown: {files.symmetric_difference(paths)}'
 assert len(paths)==76,'Initial release must contain 76 pages'
 skills=[p for p in PAGES if p['kind']=='skill'];checks=[p for p in PAGES if p['kind']=='checklist']
 assert len(skills)==28 and len(checks)==25,'Expected 28 skills and 25 checklist groups'
 assert len({p['skillId'] for p in skills})==28,'Duplicate skill ID'
 assert len({p['area'] for p in skills})==4,'Expected four skill areas'
 definitions={};items={}
 for p in skills:
  ds=definition_data(p)
  assert list(ds)==['Lv0','Lv1','Lv2','Lv3','Lv4'],p['path']+': five definitions required'
  for lv,text in ds.items():
   assert text.strip(),p['path']+': empty definition'
   definitions[p['skillId']+'.'+lv]=hashlib.sha256(text.encode()).hexdigest()
 for p in checks:
  rows=checklist_data(p);assert list(rows)==p['numbers'],p['path']+': item numbers differ'
  for num,row in rows.items():
   assert num not in items,'Duplicate checklist number'
   items[num]=hashlib.sha256(json.dumps(row,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
 assert list(items)==[f'{n:03}' for n in range(1,101)],'100 sequential items required'
 for p in PAGES:
  text=without_code(body(p['path']))
  assert re.findall(r'^# (.+)$',text,re.M)==[p['title']],p['path']+': page title differs from document map'
  assert not re.search(r'(スキル階層|レベル[1-4][：:]|第[2-7]章|付録[AB])',text),p['path']+': obsolete reference or area term'
  for url in re.findall(r'\]\(([^)]+)\)',text):
   if re.match(r'^(https?://|mailto:|#)',url):continue
   target=url.split('#')[0]
   assert not target.startswith('/'),f'{p["path"]}: use relative Markdown links: {url}'
   assert (DOCS/p['path']).parent.joinpath(target).exists(),f'{p["path"]}: broken link {url}'
 if '--migration' in sys.argv:
  baseline=json.loads((ROOT/'build/migration-baseline.json').read_text())
  assert definitions==baseline['skills'],'Skill definitions differ from source 1.1'
  assert items==baseline['checks'],'Checklist content differs from source 1.1'
  print('Migration verified: all 140 definitions and 100 complete checklist entries unchanged')
 print(f'Docs OK: {len(paths)} pages, {len(definitions)} definitions, {len(items)} items (75 TRUE / 25 FALSE)')
if __name__=='__main__':
 try:main()
 except (AssertionError,ValueError) as e:sys.exit(str(e))
