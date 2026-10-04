from pathlib import Path
import json,re,os,posixpath,unicodedata,subprocess
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
MAP=json.loads((ROOT/'build/document-map.json').read_text())
PAGES=MAP['pages']
VERSION=json.loads((ROOT/'package.json').read_text())['version']
def body(path):
 text=(DOCS/path).read_text()
 return re.sub(r'\A---\n.*?\n---\n','',text,count=1,flags=re.S).strip()
def slug(text):
 """Match VitePress heading anchors (@mdit-vue/shared slugify) so links written for the site resolve in the handbook."""
 text=unicodedata.normalize('NFKD',re.sub(r'<[^>]+>','',text).strip())
 text=re.sub(r'[\u0300-\u036f]','',text);text=re.sub(r'[\x00-\x1f]','',text)
 text=re.sub(r'[\s~`!@#$%^&*()\-_+=\[\]{}|\\;:"\'<>,.?/]+','-',text)
 text=re.sub(r'-{2,}','-',text).strip('-')
 return re.sub(r'^(\d)',r'_\1',text).lower()
def page_id(path):return path.removesuffix('.md').replace('/','-').replace('.','-')
def rel(source,target):return os.path.relpath(target,Path(source).parent).replace('\\','/')
def commit():
 try:return subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,stderr=subprocess.DEVNULL,text=True).strip()
 except (subprocess.CalledProcessError,FileNotFoundError):return 'local-uncommitted'
def without_code(text):return re.sub(r'```.*?```','',text,flags=re.S)
def definition_data(page):
 text=body(page['path'])
 return {lv:definition.strip() for lv,definition in re.findall(r'^## (Lv[0-4])\n\n(.*?)(?=^## |\Z)',text,re.M|re.S)}
def item_number(sid):
 """Sequential key (001-100) for a source ID like 2-3-1, used only for the migration baseline."""
 t,s,k=(int(x) for x in sid.split('-'));return f'{(t-1)*20+(s-1)*4+k:03}'
def checklist_data(page):
 text=body(page['path']);result={}
 for sid,section in re.findall(r'^## (\d-\d-\d)：[^\n]+\n\n(.*?)(?=^## \d-\d-\d：|\Z)',text,re.M|re.S):
  m=re.match(r'(.*?)\n\n(?:::: supplement\n.*?\n:::\n\n)?::: example\n(.*?)\n:::\n\n\[原文の参照先\]\((https://[^)]+)\)',section,re.S)
  if not m:raise ValueError(f'{page["path"]}: {sid}の構造を確認してください')
  criterion,answer,url=m.groups();num=item_number(sid)
  # The source's fourth perspective in every sub-theme is アンチパターン, whose desirable answer is FALSE.
  desired='FALSE' if int(num)%4==0 else 'TRUE';result[num]=[criterion,url,desired,answer]
 return result
