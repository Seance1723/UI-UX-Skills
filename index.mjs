import path from 'node:path';
import { fileURLToPath } from 'node:url';

const packageRoot = path.dirname(fileURLToPath(import.meta.url));

export const name = 'ui-ux-master';
export const version = '1.2.1';
export const trigger = '/ui-ux-master';

export const bins = Object.freeze({
  cli: path.join(packageRoot, 'bin', 'ui-ux-master.mjs'),
  mcp: path.join(packageRoot, 'bin', 'ui-ux-master-mcp.mjs'),
});

export const assets = Object.freeze({
  skill: path.join(packageRoot, 'SKILL.md'),
  readme: path.join(packageRoot, 'README.md'),
  llms: path.join(packageRoot, 'llms.txt'),
  manifest: path.join(packageRoot, 'ai-discovery', 'ui-ux-master.manifest.json'),
});

export function assetPath(name) {
  if (!Object.hasOwn(assets, name)) {
    throw new Error(`Unknown ui-ux-master asset: ${name}`);
  }
  return assets[name];
}
