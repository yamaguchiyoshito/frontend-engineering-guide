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
 text=re.sub(r'<[^>]+>','',text).strip().lower()
 text=re.sub(r'[^\w\-\s\u0080-\uffff]','',text)
 return re.sub(r'\s+','-',text)
def page_id(path):return path.removesuffix('.md').replace('/','-').replace('.','-')
def rel(source,target):return os.path.relpath(target,Path(source).parent).replace('\\','/')
def commit():
 try:return subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,stderr=subprocess.DEVNULL,text=True).strip()
 except (subprocess.CalledProcessError,FileNotFoundError):return 'local-uncommitted'
def without_code(text):return re.sub(r'```.*?```','',text,flags=re.S)
def definition_data(page):
 text=body(page['path'])
 return {lv:definition.strip() for lv,definition in re.findall(r'^## (Lv[0-4])\n\n(.*?)(?=^## |\Z)',text,re.M|re.S)}
def checklist_data(page):
 text=body(page['path']);result={}
 for num,section in re.findall(r'^## C(\d{3})\n\n(.*?)(?=^## C\d{3}|\Z)',text,re.M|re.S):
  m=re.search(r'\*\*チェック項目 No\.\d{3}[^*\n]*\*\*\n\n(.*?)\n\n\*\*望ましい原文への回答：(TRUE|FALSE)\*\*.*?### 望ましい回答例\n\n(.*?)\n\n\[原文の参照先\]\((https://[^)]+)\)',section,re.S)
  if not m:raise ValueError(f'{page["path"]}: C{num}の構造を確認してください')
  criterion,desired,answer,url=m.groups();result[num]=[criterion,url,desired,answer]
 return result
