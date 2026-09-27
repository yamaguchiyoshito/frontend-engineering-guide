import { spawnSync } from 'node:child_process';
for (const [command, args] of [
  ['python3', ['scripts/check_docs.py']],
  ['python3', ['scripts/build_handbook.py']],
  ['node', ['node_modules/vitepress/bin/vitepress.js', 'build', 'docs']]
]) {
  const result = spawnSync(command, args, { stdio: 'inherit', env: process.env });
  if (result.status !== 0) process.exit(result.status ?? 1);
}
