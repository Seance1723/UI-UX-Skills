'use strict';

const path = require('node:path');

const packageRoot = __dirname;

const name = 'ui-ux-master';
const version = '1.2.1';
const trigger = '/ui-ux-master';

const bins = Object.freeze({
  cli: path.join(packageRoot, 'bin', 'ui-ux-master.mjs'),
  mcp: path.join(packageRoot, 'bin', 'ui-ux-master-mcp.mjs'),
});

const assets = Object.freeze({
  skill: path.join(packageRoot, 'SKILL.md'),
  readme: path.join(packageRoot, 'README.md'),
  llms: path.join(packageRoot, 'llms.txt'),
  manifest: path.join(packageRoot, 'ai-discovery', 'ui-ux-master.manifest.json'),
});

function assetPath(name) {
  if (!Object.hasOwn(assets, name)) {
    throw new Error(`Unknown ui-ux-master asset: ${name}`);
  }
  return assets[name];
}

module.exports = {
  assetPath,
  assets,
  bins,
  name,
  trigger,
  version,
};
