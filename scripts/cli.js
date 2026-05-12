#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');

const args = process.argv.slice(2);
const command = args[0];

const scriptDir = __dirname;
const installScript = path.join(scriptDir, 'install_antigravity.sh');
const uninstallScript = path.join(scriptDir, 'uninstall_antigravity.sh');

function runScript(scriptPath, scriptArgs = []) {
  const child = spawn('bash', [scriptPath, ...scriptArgs], {
    stdio: 'inherit',
    env: { ...process.env, ANTIGRAVITY_SKILLS_DIR: process.env.ANTIGRAVITY_SKILLS_DIR }
  });

  child.on('exit', (code) => {
    process.exit(code);
  });
}

switch (command) {
  case 'install':
    runScript(installScript);
    break;
  case 'uninstall':
    runScript(uninstallScript, args.slice(1));
    break;
  case '--help':
  case '-h':
  default:
    console.log(`
Usage: enterprise-ai-skills <command> [options]

Commands:
  install           Install Enterprise AI skills to Antigravity
  uninstall         Uninstall Enterprise AI skills from Antigravity

Options:
  uninstall --remove-backups    Also remove backup directories
  -h, --help                    Show this help message
    `);
    break;
}
