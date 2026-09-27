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
 return [f'| スキルID | スキル | {header} |','| :--- | :--- | :--- |']+[row for _,row in rows]

def catalog(page):
 path=page['path'];kind=page['kind'];out=[]
 if kind=='skill-index':
  for area in MAP['areas']:
   target=f'skills/{area["id"]}/index.md';count=sum(p['kind']=='skill' and p['area']==area['id'] for p in PAGES)
   out += ['',f'## {area["title"]}（{count}スキル）','']+skill_table(path,area['id'])
 elif kind=='area':
  out=skill_table(path,page['area'])
 elif kind=='checklist-index':
  section=None
  for p in PAGES:
   if p['kind']!='checklist':continue
   if section!=p['section']:
    section=p['section'];out += ['','## '+section,'','| 原典ID | 小テーマ | 本書の項目No. |','| :--- | :--- | :--- |']
   out.append(f'| {p["sourceId"]} | [{p["title"]}]({rel(path,p["path"])}) | {p["numbers"][0]}〜{p["numbers"][-1]} |')
 elif kind=='template-index':
  out=[f'- [{p["title"]}]({rel(path,p["path"])})' for p in PAGES if p['kind']=='template']
 else:return None
 return '\n'.join(out).strip()

def sync(check=False):
 dirty=[]
 for page in PAGES:
  value=catalog(page)
  if value is None:continue
  file=DOCS/page['path'];text=file.read_text()
  new,count=re.subn(r'<!-- catalog:start -->.*?<!-- catalog:end -->',f'<!-- catalog:start -->\n\n{value}\n\n<!-- catalog:end -->',text,flags=re.S)
  if count!=1:raise ValueError(f'{file}: catalog markers missing or duplicated')
  if new!=text:
   dirty.append(page['path'])
   if not check:file.write_text(new)
 if check and dirty:raise ValueError('Run npm run docs:sync: '+', '.join(dirty))
 return dirty
if __name__=='__main__':
 try:print('Catalogs checked' if '--check' in sys.argv else 'Catalogs synchronized:',len(sync('--check' in sys.argv)))
 except ValueError as e:sys.exit(str(e))
