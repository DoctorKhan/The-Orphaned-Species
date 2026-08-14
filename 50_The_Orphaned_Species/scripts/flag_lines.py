#!/usr/bin/env python3
"""
Line-level prose flagger for Layer 1 manuscripts.
Outputs exact line numbers and content for review.
"""

from __future__ import annotations

import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
MANUSCRIPTS = BASE / "manuscripts"

BOOKS = [
    ("I", "I_The_Breach.md"),
    ("II", "II_The_Descent.md"),
    ("III", "III_The_Compact.md"),
    ("IV", "IV_The_Court_of_Threads.md"),
]

NOT_X_BUT_Y = re.compile(r"\bnot\b[^.\n]{0,30}\bbut\b", re.IGNORECASE)
STACKED_EM_DASHES = re.compile(r"—.*?—.*?—", re.DOTALL)
ECHO_CLOSER = re.compile(
    r"(?:the\s+(?:meaning|truth|point|lesson|moral|heart|essence|core|secret|gift|price|cost)\s+(?:of|was|were|is|are|had been))\b[^.\n]{0,80}\.",
    re.IGNORECASE,
)
TELL_NOT_SHOW = re.compile(
    r"\b(?:which\s+meant|in\s+other\s+words|that\s+is\s+to\s+say|in\s+effect|in\s+fact|in\s+reality|in\s+essence|really|actually|basically|essentially|simply|just|merely|only)\b",
    re.IGNORECASE,
)


def flag_book(path: Path):
    text = path.read_text()
    lines = text.split("\n")
    chapter_start = None
    chapter_title = None
    chapter_flags = {}
    results = []
    for i, line in enumerate(lines, start=1):
        if line.startswith("## Chapter"):
            if chapter_title is not None:
                results.append((chapter_title, chapter_flags))
            chapter_start = i
            chapter_title = line.strip()
            chapter_flags = {"NOT-X-BUT-Y": [], "STACKED-EM-DASHES": [], "ECHO-CLOSER": [], "TELL-NOT-SHOW": []}
            continue
        if chapter_title is None:
            continue
        # Skip blockquote headers, blank lines, markdown bold markers
        if line.startswith(">") or line.startswith("#") or not line.strip():
            continue
        if STACKED_EM_DASHES.search(line):
            chapter_flags["STACKED-EM-DASHES"].append((i, line))
        if NOT_X_BUT_Y.search(line):
            chapter_flags["NOT-X-BUT-Y"].append((i, line))
        if ECHO_CLOSER.search(line):
            chapter_flags["ECHO-CLOSER"].append((i, line))
        if TELL_NOT_SHOW.search(line):
            chapter_flags["TELL-NOT-SHOW"].append((i, line))
    if chapter_title is not None:
        results.append((chapter_title, chapter_flags))
    return results


def main():
    for code, name in BOOKS:
        path = MANUSCRIPTS / name
        print(f"\n{'='*60}")
        print(f"BOOK {code}: {name}")
        print(f"{'='*60}")
        results = flag_book(path)
        for title, flags in results:
            total = sum(len(v) for v in flags.values())
            if total == 0:
                continue
            print(f"\n{title}")
            for flag_name, items in flags.items():
                if not items:
                    continue
                print(f"  [{flag_name}] ({len(items)} hits)")
                for ln, content in items[:3]:
                    snippet = content[:140]
                    print(f"    {ln}: {snippet}")
                if len(items) > 3:
                    print(f"    ... and {len(items) - 3} more")


if __name__ == "__main__":
    main()
