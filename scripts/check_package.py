#!/usr/bin/env python3
"""Lightweight structural checks for the Officina skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "README.ja.md",
    "LICENSE",
    "package.json",
    "bin/officina-skill.js",
    "agents/openai.yaml",
    "references/labs-canon.md",
    "references/anti-patterns.md",
    "references/claimed.md",
    "references/seat.md",
    "examples/showcase.md",
    "evals/rubric.md",
    "evals/value-metrics.md",
    "evals/fixtures/generic-vs-primitive.md",
    "evals/fixtures/x-for-y.md",
    "evals/fixtures/known-platform.md",
    "evals/runs/generic-comparison.md",
    "evals/runs/README.md",
]

REQUIRED_SKILL_SECTIONS = [
    "## Core Rule",
    "## Use When",
    "## Reference Loading",
    "## Operating Discipline",
    "## Output Contract",
    "## Quality Gate",
    "## Minimal Mode",
]

BANNED_TERMS = [
    "Holy " + "Fox",
    "Ze" + "nn",
    "ze" + "nn",
    "caveman " + "prompt",
    "gen" + "shi",
    "Ha" + "ru",
    "ha" + "ru_0416",
    "@pm" + ".me",
    "/home/" + "ha" + "ru",
    "groundbreaking",
    "revolutionary",
    "truly novel",
    "game-changing",
]


def is_ignored_generated_file(path: Path) -> bool:
    relative_parts = path.relative_to(ROOT).parts
    return (
        ".git" in relative_parts
        or "__pycache__" in relative_parts
        or path.suffix in {".pyc", ".pyo"}
    )


def allows_unicode(path: Path) -> bool:
    return path.name == "README.ja.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def warn(message: str) -> None:
    print(f"WARN: {message}")


def read(path: str) -> str:
    target = ROOT / path
    if not target.exists():
        fail(f"missing required file: {path}")
    return target.read_text(encoding="utf-8")


def check_ascii(path: Path) -> None:
    data = path.read_bytes()
    for index, byte in enumerate(data):
        if byte in (9, 10, 13):
            continue
        if byte < 32 or byte > 126:
            fail(f"non-ASCII byte in {path.relative_to(ROOT)} at byte {index}")


def parse_frontmatter(skill: str) -> dict[str, str]:
    match = re.match(r"---\n(.*?)\n---\n", skill, re.DOTALL)
    if not match:
        fail("SKILL.md missing YAML frontmatter")

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def main() -> int:
    for file_name in REQUIRED_FILES:
        read(file_name)

    for path in ROOT.rglob("*"):
        if path.is_file() and not is_ignored_generated_file(path) and not allows_unicode(path):
            check_ascii(path)

    skill = read("SKILL.md")
    frontmatter = parse_frontmatter(skill)
    if frontmatter.get("name") != "officina":
        fail("SKILL.md frontmatter name must be officina")
    if not frontmatter.get("description"):
        fail("SKILL.md frontmatter description is empty")
    if len(frontmatter["description"].split()) > 80:
        fail("SKILL.md description is too long for reliable discovery")

    line_count = len(skill.splitlines())
    if line_count > 260:
        fail("SKILL.md exceeds 260 lines; move runtime detail to references")
    if line_count > 220:
        warn(f"SKILL.md is {line_count} lines; consider moving more detail to references")

    for section in REQUIRED_SKILL_SECTIONS:
        if section not in skill:
            fail(f"SKILL.md missing section: {section}")

    for reference in [
        "references/labs-canon.md",
        "references/anti-patterns.md",
        "references/claimed.md",
        "references/seat.md",
        "evals/rubric.md",
        "evals/value-metrics.md",
        "examples/showcase.md",
        "evals/fixtures/",
    ]:
        if reference not in skill:
            fail(f"SKILL.md does not mention {reference}")

    readme = read("README.md")
    for token in [
        "[Japanese](README.ja.md)",
        "Status: experimental",
        "What Changes In Practice",
        "npx officina-skill install --all",
        "npx --package github:OWNER/officina officina-skill install --all",
        "node bin/officina-skill.js install --all",
        "npx officina-skill doctor",
        "generic-comparison.md",
        "MIT. See [LICENSE](LICENSE).",
    ]:
        if token not in readme:
            fail(f"README.md missing public-readiness token: {token}")

    readme_ja = read("README.ja.md")
    for token in [
        "[English](README.md)",
        "Status: experimental",
        "Node.js 20",
        "npx officina-skill install --all",
        "npx --package github:OWNER/officina officina-skill install --all",
        "npm run check",
        "MIT. See [LICENSE](LICENSE).",
    ]:
        if token not in readme_ja:
            fail(f"README.ja.md missing Japanese-readiness token: {token}")

    package = json.loads(read("package.json"))
    if package.get("name") != "officina-skill":
        fail("package.json name must be officina-skill")
    if package.get("license") != "MIT":
        fail("package.json license must be MIT")
    if package.get("engines", {}).get("node") != ">=20":
        fail("package.json engines.node must be >=20")
    bin_map = package.get("bin", {})
    if bin_map.get("officina-skill") != "bin/officina-skill.js":
        fail("package.json missing officina-skill bin")
    if "SKILL.md" not in package.get("files", []):
        fail("package.json files must include SKILL.md")
    if "README.ja.md" not in package.get("files", []):
        fail("package.json files must include README.ja.md")

    installer = read("bin/officina-skill.js")
    for token in [
        "README.ja.md",
        "assertSafeDestination",
        "assertReplaceableDestination",
        "readInstalledSkillName",
        "Refusing target that does not end with",
        "Refusing to replace a directory that is not an",
    ]:
        if token not in installer:
            fail(f"installer missing safety token: {token}")
    if "check_package.py" in installer:
        fail("installer payload should not copy development package checks")

    all_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.rglob("*.md")
        if not is_ignored_generated_file(path) and path.name != "README.ja.md"
    )
    for term in BANNED_TERMS:
        if term in all_text:
            fail(f"banned term remains in docs: {term}")

    value_metrics = read("evals/value-metrics.md")
    for token in ["baseline", "terse", "officina", "Value Decision"]:
        if token not in value_metrics:
            fail(f"value metrics missing token: {token}")

    showcase = read("examples/showcase.md")
    for token in [
        "Shallow Baseline",
        "Officina Catalog",
        "Kill-probe",
        "Status: kill",
        "category collapse",
    ]:
        if token not in showcase:
            fail(f"showcase missing token: {token}")

    claimed = read("references/claimed.md")
    for token in ["coffer", "quaere", "ad-radicem", "munou", "dubito", "parvix"]:
        if token not in claimed:
            fail(f"claimed list missing {token}")

    print("Officina package checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
