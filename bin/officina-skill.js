#!/usr/bin/env node
"use strict";

const fs = require("fs");
const os = require("os");
const path = require("path");

const SKILL_NAME = "officina";
const PACKAGE_ROOT = path.resolve(__dirname, "..");

const DEFAULT_TARGETS = {
  codex: path.join(os.homedir(), ".codex", "skills", SKILL_NAME),
  claude: path.join(os.homedir(), ".claude", "skills", SKILL_NAME),
};

const PAYLOAD_PATHS = [
  "SKILL.md",
  "README.md",
  "README.ja.md",
  "LICENSE",
  "agents",
  "references",
  "examples",
  path.join("evals", "fixtures"),
  path.join("evals", "rubric.md"),
  path.join("evals", "value-metrics.md"),
  path.join("evals", "runs", "README.md"),
  path.join("evals", "runs", "generic-comparison.md"),
];

function printHelp() {
  console.log(`Officina skill installer

Usage:
  officina-skill install [--all|--codex|--claude] [--force] [--dry-run]
  officina-skill install --target <directory> [--force] [--dry-run]
  officina-skill doctor

Examples:
  npx officina-skill install --all
  npx officina-skill install --codex
  npx officina-skill install --claude
  npx officina-skill doctor

The installer copies this package into local skill directories:
  Codex:       ~/.codex/skills/officina
  Claude Code: ~/.claude/skills/officina
`);
}

function parseArgs(argv) {
  const args = [...argv];
  const command = args[0] && !args[0].startsWith("-") ? args.shift() : "install";
  const options = {
    command,
    codex: false,
    claude: false,
    all: false,
    force: false,
    dryRun: false,
    targets: [],
  };

  for (let i = 0; i < args.length; i += 1) {
    const arg = args[i];
    if (arg === "--codex") options.codex = true;
    else if (arg === "--claude") options.claude = true;
    else if (arg === "--all") options.all = true;
    else if (arg === "--force") options.force = true;
    else if (arg === "--dry-run") options.dryRun = true;
    else if (arg === "--help" || arg === "-h") options.command = "help";
    else if (arg === "--target") {
      const target = args[i + 1];
      if (!target) throw new Error("--target requires a directory");
      options.targets.push(resolveHome(target));
      i += 1;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  return options;
}

function resolveHome(value) {
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return path.resolve(value);
}

function copyRecursive(source, destination) {
  const stat = fs.lstatSync(source);
  if (stat.isSymbolicLink()) {
    throw new Error(`Refusing to copy symlink from package payload: ${source}`);
  }

  if (stat.isDirectory()) {
    fs.mkdirSync(destination, { recursive: true });
    for (const entry of fs.readdirSync(source)) {
      copyRecursive(path.join(source, entry), path.join(destination, entry));
    }
    return;
  }

  if (stat.isFile()) {
    fs.mkdirSync(path.dirname(destination), { recursive: true });
    fs.copyFileSync(source, destination);
  }
}

function copyPayload(destination) {
  for (const relative of PAYLOAD_PATHS) {
    const source = path.join(PACKAGE_ROOT, relative);
    if (!fs.existsSync(source)) {
      throw new Error(`Package payload is missing required path: ${relative}`);
    }
    copyRecursive(source, path.join(destination, relative));
  }
}

function assertPackageRoot() {
  const skill = path.join(PACKAGE_ROOT, "SKILL.md");
  if (!fs.existsSync(skill)) {
    throw new Error(`Cannot find SKILL.md at package root: ${PACKAGE_ROOT}`);
  }
}

function readInstalledSkillName(destination) {
  const skillPath = path.join(destination, "SKILL.md");
  if (!fs.existsSync(skillPath)) return null;

  const skill = fs.readFileSync(skillPath, "utf8");
  const frontmatter = skill.match(/^---\n([\s\S]*?)\n---\n/);
  if (!frontmatter) return null;

  for (const line of frontmatter[1].split(/\r?\n/)) {
    const match = line.match(/^name:\s*["']?([^"']+)["']?\s*$/);
    if (match) return match[1].trim();
  }
  return null;
}

function assertSafeDestination(destination) {
  if (path.basename(destination) !== SKILL_NAME) {
    throw new Error(
      `Refusing target that does not end with ${SKILL_NAME}: ${destination}`
    );
  }
}

function assertReplaceableDestination(destination) {
  const stat = fs.lstatSync(destination);
  if (stat.isSymbolicLink()) {
    throw new Error(`Refusing to replace symlink target: ${destination}`);
  }
  if (!stat.isDirectory()) {
    throw new Error(`Target exists but is not a directory: ${destination}`);
  }

  const existingName = readInstalledSkillName(destination);
  const isEmpty = fs.readdirSync(destination).length === 0;
  if (existingName === SKILL_NAME || isEmpty) return;

  throw new Error(
    `Refusing to replace a directory that is not an ${SKILL_NAME} Skill: ${destination}\n` +
      `Use a target ending in ${SKILL_NAME} that is empty or already contains this Skill.`
  );
}

function installTo(target, options) {
  const destination = path.resolve(target);
  assertSafeDestination(destination);

  if (options.dryRun) {
    console.log(`[dry-run] install ${PACKAGE_ROOT} -> ${destination}`);
    return;
  }

  if (fs.existsSync(destination)) {
    if (!options.force) {
      throw new Error(
        `Target already exists: ${destination}\n` +
          "Rerun with --force to replace it."
      );
    }
    assertReplaceableDestination(destination);
    fs.rmSync(destination, { recursive: true, force: true });
  }

  fs.mkdirSync(destination, { recursive: true });
  copyPayload(destination);
  console.log(`Installed ${SKILL_NAME} -> ${destination}`);
}

function selectedTargets(options) {
  if (options.targets.length > 0) return options.targets;

  const useAll = options.all || (!options.codex && !options.claude);
  const targets = [];
  if (useAll || options.codex) targets.push(DEFAULT_TARGETS.codex);
  if (useAll || options.claude) targets.push(DEFAULT_TARGETS.claude);
  return targets;
}

function doctor() {
  for (const [name, target] of Object.entries(DEFAULT_TARGETS)) {
    const skillPath = path.join(target, "SKILL.md");
    const status = fs.existsSync(skillPath) ? "installed" : "missing";
    console.log(`${name}: ${status} (${target})`);
  }
}

function main() {
  const options = parseArgs(process.argv.slice(2));

  if (options.command === "help") {
    printHelp();
    return;
  }

  if (options.command === "doctor") {
    doctor();
    return;
  }

  if (options.command !== "install") {
    throw new Error(`Unknown command: ${options.command}`);
  }

  assertPackageRoot();
  for (const target of selectedTargets(options)) {
    installTo(target, options);
  }
}

try {
  main();
} catch (error) {
  console.error(`officina-skill: ${error.message}`);
  process.exit(1);
}
