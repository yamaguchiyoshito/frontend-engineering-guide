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
 assert len(paths)==83,'Expected 83 pages'
 skills=[p for p in PAGES if p['kind']=='skill'];checks=[p for p in PAGES if p['kind']=='checklist']
 assert len(skills)==31 and len(checks)==25,'Expected 31 skills and 25 checklist groups'
 assert len({p['skillId'] for p in skills})==31,'Duplicate skill ID'
 assert len({p['area'] for p in skills})==4,'Expected four skill areas'
 definitions={};items={}
 for p in skills:
  ds=definition_data(p)
  assert list(ds)==['Lv0','Lv1','Lv2','Lv3','Lv4'],p['path']+': five definitions required'
  for lv,text in ds.items():
   assert text.strip(),p['path']+': empty definition'
   definitions[p['skillId']+'.'+lv]=hashlib.sha256(text.encode()).hexdigest()
 references=json.loads((ROOT/'build/references.json').read_text())
 for p in skills:
  text=body(p['path']);starts=re.findall(r'^::: start\n(.*?)\n:::$',text,re.M|re.S)
  assert len(starts)==1 and '## Lv0' in text.split(starts[0])[1][:12],p['path']+': one ::: start block is required right before ## Lv0'
  urls=re.findall(r'\]\((https?://[^)]+)\)',starts[0]);entry=references['skills'][p['skillId']]
  first=[r['url'] for key in ('docs','tools') for r in entry.get(key,[]) if r.get('start')]
  assert len(first)==1,p['path']+': exactly one reference must be marked start'
  assert urls==first,p['path']+': the ::: start block must link the reference marked start'
 for p in checks:
  rows=checklist_data(p);assert list(rows)==[item_number(f'{p["sourceId"]}-{k}') for k in range(1,5)],p['path']+': item IDs differ'
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
 glossary=json.loads((ROOT/'build/glossary.json').read_text());terms=glossary['terms']
 ids=[t['id'] for t in terms];names=[t['term'] for t in terms];anchors=[slug(n) for n in names]
 assert len(ids)==len(set(ids)) and len(names)==len(set(names)) and len(anchors)==len(set(anchors)),'Glossary terms must be unique'
 refs={p.get('skillId') for p in skills}|{p.get('sourceId') for p in checks}|set(paths)
 for t in terms:
  assert t['category'] in glossary['categories'],t['id']+': unknown category'
  assert t['definition'].strip(),t['id']+': empty definition'
  for ref in t.get('see',[]):assert ref in refs,t['id']+': unknown related page '+ref
 for path,tids in glossary['pages'].items():
  assert path in paths,'glossary.pages: unknown page '+path
  assert tids and len(tids)==len(set(tids)) and all(i in ids for i in tids),'glossary.pages: bad term list for '+path
 for p in skills+checks:assert p['path'] in glossary['pages'],p['path']+': add its terms to build/glossary.json'
 learning=json.loads((ROOT/'build/learning.json').read_text());skill_ids={p['skillId'] for p in skills}
 for r in learning['courses']:
  assert all(r.get(k) for k in ('title','url','note','lang','format','skills')),'learning.json: incomplete course '+r.get('title','?')
  assert r['lang'] in ('ja','en') and r['format'] in ('読む','手を動かす','動画'),'learning.json: bad lang/format for '+r['title']
  assert all(s in skill_ids for s in r['skills']),'learning.json: unknown skill in '+r['title']
 for r in learning['maps']:assert all(r.get(k) for k in ('title','url','note')),'learning.json: incomplete map'
 if '--migration' in sys.argv:
  baseline=json.loads((ROOT/'build/migration-baseline.json').read_text())
  assert definitions==baseline['skills'],'Skill definitions differ from the migration baseline'
  assert items==baseline['checks'],'Checklist content differs from source 1.1'
  print(f'Migration verified: all {len(definitions)} definitions and 100 complete checklist entries unchanged')
 print(f'Docs OK: {len(paths)} pages, {len(definitions)} definitions, {len(items)} items (75 TRUE / 25 FALSE), {len(terms)} glossary terms, {len(learning["courses"])} courses')
if __name__=='__main__':
 try:main()
 except (AssertionError,ValueError) as e:sys.exit(str(e))
