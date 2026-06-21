#!/usr/bin/env python3
"""Seed Hermes documentation from the local skill file (offline alternative)."""
import shutil, sys, os
from datetime import datetime, timezone

HUMAN = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "human", "hermes")
os.makedirs(HUMAN, exist_ok=True)

# The Hermes skill file is the best offline reference for the full docs
skill_paths = [
    os.path.expanduser("~/.hermes/skills/autonomous-ai-agents/hermes-agent/SKILL.md"),
    # Also check alternative location
    os.path.expanduser("~/AppData/Local/hermes/skills/autonomous-ai-agents/hermes-agent/SKILL.md"),
]

src = None
for p in skill_paths:
    if os.path.exists(p):
        src = p
        break

if not src:
    print("ERROR: Cannot find Hermes agent skill file.", file=sys.stderr)
    print("Checked:")
    for p in skill_paths:
        print(f"  - {p}", file=sys.stderr)
    sys.exit(1)

# Read skill file and add frontmatter
with open(src, "r", encoding="utf-8") as f:
    content = f.read()

# Strip skill frontmatter (--- ... ---) if present
if content.startswith("---"):
    end = content.find("---", 3)
    if end != -1:
        content = content[end+3:].strip()

out_path = os.path.join(HUMAN, "_skill-docs.md")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(f"""---
title: Hermes Agent — Full Skill Documentation
source: hermes
url: {src}
fetched: {datetime.now(timezone.utc).isoformat()}
note: Offline copy from the installed hermes-agent skill file.
      Covers CLI commands, slash commands, config, providers, toolsets,
      security, voice/STT/TTS, spawning agents, troubleshooting, and contributor guide.
---

{content}
""")

print(f"Seeded: {out_path} ({os.path.getsize(out_path)} bytes)")
