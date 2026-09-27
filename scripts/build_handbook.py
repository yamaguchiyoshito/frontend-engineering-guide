"""Generate one portable Markdown handbook and blank forms from docs only."""
from common import *
from datetime import datetime,timezone
from zipfile import ZipFile,ZIP_DEFLATED
import shutil,hashlib
selected=[p for p in PAGES if p['handbook']]
ids={p['path']:page_id(p['path']) for p in selected}
ids.update({'index.md':'top','downloads.md':'download-files'})
revision=commit();date=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
out=ROOT/'dist';public=DOCS/'public/downloads'
out.mkdir(exist_ok=True);public.mkdir(parents=True,exist_ok=True)
for f in public.iterdir():
 if f.is_file():f.unlink()
provenance=f'版：{VERSION}  \n生成元コミット：{revision}  \n生成日時（UTC）：{date}'
handbook=[f'<a id="top"></a>\n\n# {MAP["title"]}\n\n{provenance}\n\n公開基準と架空の回答例を収録しています。実際の評価記録は含みません。\n\nチームチェックリストの原文は、一般社団法人日本CTO協会「Webフロントエンド版DX Criteria（v202402）」（https://dxcriteria.cto-a.org/frontend）です。出典はCC BY-SA 4.0（https://creativecommons.org/licenses/by-sa/4.0/deed.ja）で提供されており、本文書全体も同じライセンスで提供します。\n\n## 目次\n']
handbook.extend(f'- [{p["title"]}](#{ids[p["path"]]})' for p in selected)
linkre=re.compile(r'\]\(([^)]+)\)')
for p in selected:
 path=p['path'];text=body(path)
 text=re.sub(r'<!-- (?:catalog|template):(start|end) -->\n?','',text)
 text=re.sub(r'^::: example\n(.*?)\n:::$',lambda m:'> **望ましい回答例**（架空の記入例）\n>\n'+'\n'.join('> '+l if l else '>' for l in m.group(1).split('\n')),text,flags=re.M|re.S)
 def convert(m):
  url=m.group(1)
  if re.match(r'^(https?://|mailto:)',url):return m.group(0)
  target,_,anchor=url.partition('#')
  target=posixpath.normpath(posixpath.join(posixpath.dirname(path),target)) if target else path
  if target not in ids:raise ValueError(f'{path}: handbook target not included: {url}')
  return f'](#{ids[target]}'+('--'+anchor if anchor else '')+')'
 lines=[];fenced=False;seen={}
 for line in text.splitlines():
  if line.startswith('```'):fenced=not fenced;lines.append(line);continue
  if fenced:lines.append(line);continue
  line=linkre.sub(convert,line)
  m=re.match(r'^(#{1,6}) (.*)$',line)
  if m:
   depth,title=m.groups();anchor=ids[path]
   if len(depth)>1:
    stem=slug(title);count=seen.get(stem,0);seen[stem]=count+1
    anchor+='--'+stem+(f'-{count}' if count else '')
   lines.extend([f'<a id="{anchor}"></a>','',('#'*min(len(depth)+1,6))+' '+title])
  else:lines.append(line)
 handbook.append('\n\n---\n\n'+'\n'.join(lines))
handbook.append('\n\n<a id="download-files"></a>\n\n## ダウンロードファイルについて\n\n本ファイルはサイトの正本から生成しています。空の記録書式は以下のテンプレート欄からコピーできます。配布ZIPにも同じ書式を収録しています。')
book='\n'.join(handbook)+'\n'
anchors=re.findall(r'<a id="([^"]+)"></a>',book)
assert len(anchors)==len(set(anchors)),'Handbook anchor collision'
for anchor in re.findall(r'\]\(#([^)]+)\)',without_code(book)):
 assert anchor in anchors,'Broken handbook anchor: '+anchor
filename=f'frontend-handbook-v{VERSION}.md'
(out/'frontend-handbook.md').write_text(book);(public/filename).write_text(book)
files=[{'name':filename,'title':'全編を読む：単一Markdown','description':'使い方・28の要素技術・100項目・書式・運用'}]
forms=[]
for p in PAGES:
 if p['kind']!='template':continue
 m=re.search(r'<!-- template:start -->\n```markdown\n(.*?)\n```\n<!-- template:end -->',body(p['path']),re.S)
 if not m:raise ValueError('Template block not found: '+p['path'])
 form=m.group(1)+'\n\n---\n\n'+provenance+'\n'
 name=Path(p['path']).name;(public/name).write_text(form);forms.append(name)
 files.append({'name':name,'title':p['title'],'description':'空のMarkdown書式'})
zipname=f'frontend-templates-v{VERSION}.zip'
with ZipFile(public/zipname,'w',ZIP_DEFLATED) as z:
 for name in forms:z.write(public/name,arcname=name)
files.insert(1,{'name':zipname,'title':'記録書式をまとめて取得','description':'4種類のMarkdownを収録したZIP'})
for f in files:
 data=(public/f['name']).read_bytes();f.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
manifest={'version':VERSION,'commit':revision,'generatedAt':date,'files':files}
(public/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
shutil.copy(public/'manifest.json',out/'download-manifest.json')
print(f'Downloads OK: handbook ({len(book.encode()):,} bytes), 4 blank forms, ZIP, provenance and SHA-256')
