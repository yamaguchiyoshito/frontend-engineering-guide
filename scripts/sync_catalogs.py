"""Keep GitHub-readable catalog blocks aligned with the single document map."""
from common import *
import sys

def skill_table(path,area):
 rows=[]
 for p in PAGES:
  if p['kind']=='skill' and p['area']==area:
   label,prerequisite=re.search(r'\*\*(評価対象|主な前提)：\*\* (.+)',body(p['path'])).groups()
   rows.append((label,f'| `{p["skillId"]}` | [{p["title"]}]({rel(path,p["path"])}) | {prerequisite.strip()} |'))
 labels={label for label,_ in rows};header=labels.pop() if len(labels)==1 else '評価対象・主な前提'
 return [f'| ID | 要素技術 | {header} |','| :--- | :--- | :--- |']+[row for _,row in rows]

def catalog(page):
 path=page['path'];kind=page['kind'];out=[]
 if kind=='skill-index':
  for area in MAP['areas']:
   target=f'skills/{area["id"]}/index.md';count=sum(p['kind']=='skill' and p['area']==area['id'] for p in PAGES)
   out += ['',f'## {area["title"]}（{count}つの要素技術）' if count<10 else f'## {area["title"]}（{count}の要素技術）','']+skill_table(path,area['id'])
 elif kind=='area':
  out=skill_table(path,page['area'])
 elif kind=='checklist-index':
  section=None
  for p in PAGES:
   if p['kind']!='checklist':continue
   if section!=p['section']:
    section=p['section'];out += ['','## '+section,'','| ID | 小テーマ |','| :--- | :--- |']
   out.append(f'| {p["sourceId"]} | [{p["title"]}]({rel(path,p["path"])}) |')
 elif kind=='template-index':
  out=[f'- [{p["title"]}]({rel(path,p["path"])})' for p in PAGES if p['kind']=='template']
 else:return None
 return '\n'.join(out).strip()

REFERENCES=json.loads((ROOT/'build/references.json').read_text())
def link(page,r):
 return '- '+('**まず読む** ' if r.get('start') else '')+f'[{r["title"]}]({r["url"]})'+('（出典で言及）' if r.get('cited') else '')+f' — {r["note"]}'
def references(page):
 path=page['path'];selection=f'選定は[技術選定]({rel(path,"checklists/technology-selection.md")})の観点で行ってください。'
 if page['kind']=='skill':
  entry=REFERENCES['skills'][page['skillId']]
  out=[f'{REFERENCES["note"]}{selection}{REFERENCES["checked"]}確認。']
  sections=[('docs','仕様・公式ドキュメント'),('tools','代表的なライブラリ・ツール')]
 elif page['kind']=='checklist':
  entry=REFERENCES['checklists'][page['sourceId']]
  out=[f'{REFERENCES["note_checklist"]}{selection}{REFERENCES["checked"]}確認。']
  sections=[('guides','指針・標準'),('tools','代表的なツール・サービス')]
 else:return None
 for key,label in sections:
  if entry.get(key):out += ['',f'**{label}**','']+[link(page,r) for r in entry[key]]
 return '\n'.join(out)
def related_skills(page):
 """Checklist pages list their related element technologies in the header, next to the glossary terms."""
 entry=REFERENCES['checklists'][page['sourceId']];pages={p['skillId']:p for p in PAGES if p['kind']=='skill'};paths={p['path']:p for p in PAGES}
 items=[f'[{(pages.get(s) or paths[s])["title"]}]({rel(page["path"],(pages.get(s) or paths[s])["path"])})' for s in entry.get('skills',[])]
 return '**関連する要素技術：** '+'、'.join(items)

GLOSSARY=json.loads((ROOT/'build/glossary.json').read_text())
TERMS={t['id']:t for t in GLOSSARY['terms']}
GLOSSARY_PATH='guide/glossary.md'
def related(path,ref):
 """Resolve a glossary 'see' entry (skill ID, checklist source ID or page path) to a link."""
 for p in PAGES:
  if p.get('skillId')==ref:return f'[{p["title"]}]({rel(path,p["path"])})'
  if p.get('sourceId')==ref:return f'[{p["sourceId"]} {p["title"]}]({rel(path,p["path"])})'
  if p['path']==ref:return f'[{p["title"]}]({rel(path,p["path"])})'
 raise ValueError(f'glossary: unknown reference {ref}')
def glossary(page):
 if page['path']!=GLOSSARY_PATH:return None
 path=page['path'];out=[GLOSSARY['note']]
 for category in GLOSSARY['categories']:
  out += ['',f'## {category}']
  for t in GLOSSARY['terms']:
   if t['category']!=category:continue
   out += ['',f'### {t["term"]}','',t['definition']]
   if t.get('see'):out += ['','関連：'+'、'.join(related(path,ref) for ref in t['see'])]
 return '\n'.join(out)
def terms(page):
 ids=GLOSSARY['pages'].get(page['path'])
 if not ids:return None
 target=rel(page['path'],GLOSSARY_PATH)
 line='**前提となる用語：** '+'、'.join(f'[{TERMS[i]["term"]}]({target}#{slug(TERMS[i]["term"])})' for i in ids)
 return line+('  \n'+related_skills(page) if page['kind']=='checklist' else '')

LEARNING=json.loads((ROOT/'build/learning.json').read_text())
LEARNING_PATH='guide/learning.md'
def first_step(page):
 """The task sentence(s) of a skill page's ::: start block, without the trailing まず読む link."""
 m=re.search(r'^::: start\n(.*?)\n:::$',body(page['path']),re.M|re.S)
 return re.sub(r'まず読む：\[[^\]]*\]\([^)]*\)\s*$','',m.group(1)).strip()
def start_reference(skill_id):
 entry=REFERENCES['skills'][skill_id]
 return [r for key in ('docs','tools') for r in entry.get(key,[]) if r.get('start')][0]
def route(page):
 if page['path']!=LEARNING_PATH:return None
 path=page['path'];out=[]
 for area in MAP['areas']:
  out += ['',f'### {area["title"]}','']
  n=0
  for p in PAGES:
   if p['kind']!='skill' or p['area']!=area['id']:continue
   n+=1;label,prerequisite=re.search(r'\*\*(評価対象|主な前提)：\*\* (.+)',body(p['path'])).groups();start=start_reference(p['skillId'])
   out.append(f'{n}. **[{p["title"]}]({rel(path,p["path"])})**（{label}：{prerequisite.strip()}）  \n   まず読む：[{start["title"]}]({start["url"]})  \n   Lv1の入口となる課題：{first_step(p)}')
 return '\n'.join(out).strip()
def courses(page):
 if page['path']!=LEARNING_PATH:return None
 path=page['path'];pages={p['skillId']:p for p in PAGES if p['kind']=='skill'};area_of={p['skillId']:p['area'] for p in pages.values()}
 def item(r):
  skills='、'.join(f'[{pages[s]["title"]}]({rel(path,pages[s]["path"])})' for s in r.get('skills',[]))
  return f'- [{r["title"]}]({r["url"]})'+('（英語）' if r.get('lang')=='en' else '')+f' — {r["note"]}。形式：{r["format"]}。対応：{skills}'
 out=[f'{LEARNING["note"]}{LEARNING["checked"]}確認。','','## 体系的なコース','','領域をまたいで通しで学べる無料のコースです。日本語の資料を優先し、英語のみの資料には（英語）と付記しています。']
 for area in MAP['areas']:
  rows=[item(r) for r in LEARNING['courses'] if area_of[r['skills'][0]]==area['id']]
  if rows:out += ['',f'### {area["title"]}','']+rows
 out += ['','## 全体地図','','学習項目の全体像を見渡すための外部の地図です。分類は本書の要素技術と一致しないため、対応する領域や要素技術を付記しています。','']+[f'- [{r["title"]}]({r["url"]})（英語） — {r["note"]}' for r in LEARNING['maps']]
 return '\n'.join(out)

def blocks(page):
 for marker,value in [('catalog',catalog(page)),('references',references(page)),('terms',terms(page)),('glossary',glossary(page)),('route',route(page)),('courses',courses(page))]:
  if value is not None:yield marker,value

def sync(check=False):
 dirty=[]
 for page in PAGES:
  for marker,value in blocks(page):
   file=DOCS/page['path'];text=file.read_text()
   new,count=re.subn(rf'<!-- {marker}:start -->.*?<!-- {marker}:end -->',f'<!-- {marker}:start -->\n\n{value}\n\n<!-- {marker}:end -->',text,flags=re.S)
   if count!=1:raise ValueError(f'{file}: {marker} markers missing or duplicated')
   if new!=text:
    dirty.append(page['path'])
    if not check:file.write_text(new)
 if check and dirty:raise ValueError('Run npm run docs:sync: '+', '.join(dirty))
 return dirty
if __name__=='__main__':
 try:print('Catalogs checked' if '--check' in sys.argv else 'Catalogs synchronized:',len(sync('--check' in sys.argv)))
 except ValueError as e:sys.exit(str(e))
