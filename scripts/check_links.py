"""Check that every external link in build/references.json responds. Run on a schedule, not on every PR."""
import json,sys,urllib.request,urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'build/references.json').read_text())
links=[(sid,r['url']) for sid,entry in data['skills'].items() for key in ('docs','tools') for r in entry[key]]
failed=[]
for sid,url in links:
 for method in ('HEAD','GET'):
  try:
   req=urllib.request.Request(url,method=method,headers={'User-Agent':'Mozilla/5.0 (compatible; frontend-engineering-guide link check)','Accept':'*/*'})
   with urllib.request.urlopen(req,timeout=20) as res:
    status=res.status
   break
  except urllib.error.HTTPError as e:
   status=e.code
   if method=='GET' or status not in (403,405):break
  except Exception as e:
   status=str(e)
   if method=='GET':break
 ok=isinstance(status,int) and status<400
 print(('ok  ' if ok else 'FAIL'),sid,url,status)
 if not ok:failed.append((sid,url,status))
print(f'{len(links)-len(failed)}/{len(links)} links reachable')
if failed:
 print('Unreachable links:');[print(f'  {sid}: {url} ({status})') for sid,url,status in failed]
 sys.exit(1)
