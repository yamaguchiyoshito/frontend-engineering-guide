"""Check every built page, local asset/link and heading target without network."""
from common import *
from html.parser import HTMLParser
from urllib.parse import urljoin,urlparse,unquote
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.refs=[];self.lang=None
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if 'id' in attrs:self.ids.add(attrs['id'])
  if tag=='html':self.lang=attrs.get('lang')
  for a in ['href','src']:
   if a in attrs:self.refs.append(attrs[a])
site=DOCS/'.vitepress/dist'
first=(site/'index.html').read_text()
base=re.search(r'href="([^"]*)assets/favicon.svg"',first).group(1)
origin='https://site.test';parsers={};count=0
for path in site.rglob('*.html'):
 parser=Parser();parser.feed(path.read_text());parsers[path]=parser
 assert parser.lang=='ja-JP',f'Language missing: {path}'
for path,parser in parsers.items():
 current=origin+base+path.relative_to(site).as_posix()
 for ref in parser.refs:
  if ref.startswith(('mailto:','tel:','data:')):continue
  url=urlparse(urljoin(current,ref))
  if url.netloc!='site.test':continue
  decoded=unquote(url.path)
  assert decoded.startswith(base),f'{path}: link escapes site base: {ref}'
  relative=decoded[len(base):];target=site/relative
  if relative.endswith('/') or target.is_dir():target=target/'index.html'
  elif not target.suffix:target=target.with_suffix('.html')
  assert target.is_file(),f'{path.relative_to(site)}: missing {ref}'
  if url.fragment and target.suffix=='.html':
   assert unquote(url.fragment) in parsers[target].ids,f'{path.relative_to(site)}: unknown anchor {ref}'
  count+=1
assert len(parsers)==86,f'Expected 85 pages + 404; got {len(parsers)}'
manifest=json.loads((site/'downloads/manifest.json').read_text())
import hashlib
for item in manifest['files']:
 data=(site/'downloads'/item['name']).read_bytes()
 assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256'],item['name']
print(f'HTML OK: {len(parsers)} pages including 404; {count} local links/assets/anchors; 6 downloads; base={base}')
