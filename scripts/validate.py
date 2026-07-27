#!/usr/bin/env python3
import re
import sys
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILL_MD = REPO_ROOT / "SKILL.md"
TRACKER = REPO_ROOT / "dok-tracker.template.md"
LICENSE = REPO_ROOT / "LICENSE"
README = REPO_ROOT / "README.md"

failures = []


def check(name, condition, detail=""):
    if not condition:
        msg = f"FAIL: {name}"
        if detail:
            msg += f" - {detail}"
        failures.append(msg)
        print(f"  ✗ {name}" + (f" ({detail})" if detail else ""))
    else:
        print(f"  ✓ {name}")


def main():
    print("=== File Structure ===")
    check("SKILL.md exists", SKILL_MD.exists())
    check("dok-tracker.template.md exists", TRACKER.exists())
    check("LICENSE exists", LICENSE.exists())
    check("README.md exists", README.exists())

    if not SKILL_MD.exists():
        print("\nCannot continue without SKILL.md")
        sys.exit(1)

    content = SKILL_MD.read_text()
    body = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)

    print("\n=== Frontmatter ===")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    check("Has YAML frontmatter", match is not None)

    if match:
        try:
            fm = yaml.safe_load(match.group(1))
            check("Frontmatter is valid YAML", isinstance(fm, dict))
            check("Has 'name' field", "name" in fm)
            check("Has 'description' field", "description" in fm)
            check("Has 'license' field", "license" in fm)

            allowed = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
            unexpected = set(fm.keys()) - allowed
            check(
                "No fields that break Claude Desktop validator",
                len(unexpected) == 0,
                f"unexpected: {unexpected}" if unexpected else "",
            )

            desc = fm.get("description", "")
            check("Description under 1024 chars", len(desc) <= 1024, f"got {len(desc)}")
            check("No angle brackets in description", "<" not in desc and ">" not in desc)

            name = fm.get("name", "")
            check("Name is kebab-case", bool(re.match(r"^[a-z0-9-]+$", name)), f"got '{name}'")
        except yaml.YAMLError as e:
            check("Frontmatter parses", False, str(e))

    print("\n=== Protocol Content ===")
    sections = [
        "The Core Problem",
        "The 4-Tier Expert Engineer Model",
        "Depth of Knowledge (DOK) Levels",
        "Activation",
        "The Learning Mode Contract",
        "Progressive Disclosure and the Why Stack",
        "Make It Concrete (Analogies)",
        "Micro-Challenges",
        "Graduation Signals",
        "PR Review in Learning Mode",
        "Session Logging",
        "Anti-Patterns",
        "Configuration",
        "Commands Reference",
        "Philosophy",
    ]
    for section in sections:
        check(f"Section: {section}", section in content)

    print("\n=== Style Rules ===")
    check("No em dashes", "\u2014" not in content)
    body_lines = body.split("\n")
    blockquotes = [l for l in body_lines if l.strip().startswith(">")]
    check("No block quotes in body", len(blockquotes) == 0, f"found {len(blockquotes)} lines")

    print("\n=== No Personal References ===")
    personal_refs = ["Dakota", "TIDAL", "tidal", "the_professional", "dakotaos", "~/Development"]
    found = [r for r in personal_refs if r in body]
    check("No personal/company references in protocol body", len(found) == 0, f"found: {found}")

    print("\n=== Size Check ===")
    token_estimate = len(content) // 4
    check("Under 6000 tokens", token_estimate < 6000, f"~{token_estimate} tokens")

    print("\n=== DOK Tracker Template ===")
    if TRACKER.exists():
        tracker_content = TRACKER.read_text()
        check("Has tier reference", "Tier Reference" in tracker_content)
        check("Has DOK reference", "DOK Level Reference" in tracker_content)
        check("Has skills tracker table", "| Skill |" in tracker_content)
        check("Has progression log", "Progression Log" in tracker_content)

    print("\n=== README ===")
    if README.exists():
        readme = README.read_text()
        check("Has npx install command", "npx skills add dakotafabro/learning-mode -g" in readme)
        check("Has Claude Desktop instructions", ".skill" in readme)
        check("Has compatibility matrix", "Goose CLI" in readme and "Claude Desktop" in readme)
        check("Has config block example", "Strong platform" in readme)

    print("\n" + "=" * 40)
    if failures:
        print(f"FAILED: {len(failures)} check(s)")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("ALL CHECKS PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
