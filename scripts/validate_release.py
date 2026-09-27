"""Validate an existing release tag before checkout/deployment. No tag is created."""
import json,re,subprocess,sys

def run(*args):return subprocess.check_output(['git',*args],text=True,stderr=subprocess.DEVNULL).strip()
def validate(tag):
 if not re.fullmatch(r'v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)',tag):raise ValueError('release_tag must be vX.Y.Z')
 ref='refs/tags/'+tag
 sha=run('rev-parse','--verify',ref+'^{commit}')
 if subprocess.run(['git','merge-base','--is-ancestor',sha,'origin/main']).returncode!=0:raise ValueError('Tag must refer to a commit included in origin/main')
 version=json.loads(run('show',ref+':package.json'))['version']
 if tag!='v'+version:raise ValueError('Tag and package.json version must match')
 return sha
if __name__=='__main__':
 try:print(validate(sys.argv[1]))
 except (IndexError,ValueError,subprocess.CalledProcessError) as e:sys.exit(str(e))
