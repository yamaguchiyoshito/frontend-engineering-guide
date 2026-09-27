"""Exercise the release boundary in an isolated repository with real Git refs."""
import json,subprocess,tempfile,unittest,os
from pathlib import Path
from validate_release import validate
class ReleaseTest(unittest.TestCase):
 def setUp(self):
  self.previous=Path.cwd();self.tmp=tempfile.TemporaryDirectory();os.chdir(self.tmp.name)
  self.git('init','-b','main','--quiet');self.git('config','user.name','Release test');self.git('config','user.email','release-test@example.invalid')
  Path('package.json').write_text(json.dumps({'version':'1.2.0'}))
  self.git('add','package.json');self.git('commit','--quiet','-m','Release fixture')
  self.git('update-ref','refs/remotes/origin/main','HEAD');self.git('tag','v1.2.0')
 def tearDown(self):os.chdir(self.previous);self.tmp.cleanup()
 def git(self,*args):return subprocess.check_output(['git',*args],text=True,stderr=subprocess.DEVNULL).strip()
 def test_valid_tag(self):self.assertEqual(validate('v1.2.0'),self.git('rev-parse','HEAD'))
 def test_wrong_version(self):
  self.git('tag','v1.2.1')
  with self.assertRaisesRegex(ValueError,'version'):validate('v1.2.1')
 def test_unmerged_commit(self):
  self.git('checkout','-b','feature','--quiet');Path('package.json').write_text(json.dumps({'version':'1.3.0'}))
  self.git('commit','-am','Unmerged release','--quiet');self.git('tag','v1.3.0')
  with self.assertRaisesRegex(ValueError,'origin/main'):validate('v1.3.0')
 def test_invalid_ref(self):
  for ref in ['main','v1.2.0; echo bad','refs/tags/v1.2.0','v01.2.0','v1.2.0-beta']:
   with self.subTest(ref=ref),self.assertRaisesRegex(ValueError,'vX.Y.Z'):validate(ref)
 def test_missing_tag(self):
  with self.assertRaises(subprocess.CalledProcessError):validate('v9.9.9')
if __name__=='__main__':unittest.main()
