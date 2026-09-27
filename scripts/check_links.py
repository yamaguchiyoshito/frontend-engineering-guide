"""Check that every external link in build/references.json and build/learning.json responds. Run on a schedule, not on every PR."""
import json,sys,time,urllib.request,urllib.error,urllib.parse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'build/references.json').read_text())
links=[];skipped=[]
for group in ('skills','checklists'):
 for sid,entry in data.get(group,{}).items():
  for key in ('docs','tools','guides'):
   for r in entry.get(key,[]):
    (skipped if r.get('check') is False else links).append((sid,r['url']))
def probe(url):
 target=urllib.parse.quote(url,safe=':/?&=#%+~@!$,;()*')
 for method in ('HEAD','GET'):
  try:
   req=urllib.request.Request(target,method=method,headers={'User-Agent':'Mozilla/5.0 (compatible; frontend-engineering-guide link check)','Accept':'*/*','Accept-Language':'ja,en'})
   with urllib.request.urlopen(req,timeout=20) as res:
    return res.status
  except urllib.error.HTTPError as e:
   status=e.code
   if method=='GET' or status not in (403,405):return status
  except Exception as e:
   status=str(e)
   if method=='GET':return status
 return status
learning=json.loads((ROOT/'build/learning.json').read_text())
for r in learning.get('courses',[])+learning.get('maps',[]):
 (skipped if r.get('check') is False else links).append(('learning',r['url']))
failed=[]
for sid,url in links:
 status=probe(url)
 if not (isinstance(status,int) and status<400):
  # Some help centers answer 404 intermittently; one retry after a pause separates a flaky answer from a dead link.
  time.sleep(3);status=probe(url)
 ok=isinstance(status,int) and status<400
 print(('ok  ' if ok else 'FAIL'),sid,url,status)
 if not ok:failed.append((sid,url,status))
for sid,url in skipped:print('skip',sid,url,'(check: false)')
print(f'{len(links)-len(failed)}/{len(links)} links reachable, {len(skipped)} skipped')
if failed:
 print('Unreachable links:');[print(f'  {sid}: {url} ({status})') for sid,url,status in failed]
 sys.exit(1)
