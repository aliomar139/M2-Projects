import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire('C:/Users/user/AppData/Local/OpenAI/Codex/runtimes/cua_node/45309f9050f7314b/bin/node_modules/__runtime__.cjs');
const sharp = require('sharp');
const dir = process.argv[2];
const names = (await fs.readdir(dir)).filter(n=>n.endsWith('.svg'));
for (const name of names) {
  const png = path.join(dir,name.replace(/\.svg$/,'.png'));
  await sharp(path.join(dir,name),{density:120}).png().toFile(png);
}
console.log(`Rendered ${names.length} images in ${dir}`);
