#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

MANUSCRIPT_ROOTS = [
    ROOT / "manuscripts",
    ROOT / "50_The_Orphaned_Species" / "manuscripts",
]

EXCLUDE_DIRS = {".git", "node_modules", "venv", ".venv", "dist", "build"}
EXCLUDE_FILES = {"audit_temp_findings.json", "README.md"}


def is_excluded(path: Path) -> bool:
    return (
        any(part in EXCLUDE_DIRS for part in path.parts)
        or path.name in EXCLUDE_FILES
        or path.suffix.lower() != ".md"
    )


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def collect_manuscripts():
    files = []
    for root in MANUSCRIPT_ROOTS:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if is_excluded(path):
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            files.append((path, word_count(text)))
    return files


def label_for(path: Path) -> str:
    rel = path.relative_to(ROOT)
    parts = rel.parts
    if "manuscripts" in parts:
        idx = parts.index("manuscripts")
        after = parts[idx + 1 :]
        if len(after) == 1:
            return after[0].replace(".md", "")
        name = after[-1].replace(".md", "")
        parent = after[-2].replace(".md", "") if len(after) > 1 else ""
        return f"{parent}/{name}" if parent else name
    return str(rel)


def book_group(label: str) -> str:
    m = re.match(r"^(I{1,3}|IV|V)[_/]", label)
    if m:
        return m.group(1)
    if "book_i_chapters" in label:
        return "I"
    return "Other"


def main():
    files = collect_manuscripts()
    if not files:
        print("No manuscript files found.")
        return

    rows = []
    total_words = 0
    for path, wc in files:
        label = label_for(path)
        book = book_group(label)
        pages = wc / 250.0
        rows.append((book, label, wc, pages))
        total_words += wc

    # Group by book
    groups = {}
    order = []
    for book, label, wc, pages in rows:
        groups.setdefault(book, []).append((label, wc, pages))
        if book not in order:
            order.append(book)

    total_pages = total_words / 250.0

    # Standard novel targets
    targets = [
        ("100k", 100_000),
        ("120k", 120_000),
        ("140k", 140_000),
        ("180k", 180_000),
    ]

    def pct_bar(pct: float, width: int = 20) -> str:
        pct = max(0.0, min(pct, 1.0))
        filled = int(pct * width)
        return f"[{'=' * filled}{' ' * (width - filled)}] {pct * 100:.1f}%"

    header = f"{'Book':<8} {'File':<42} {'Words':>10} {'Pages':>8}"
    sep = "─" * 74

    print()
    for book in order:
        print(f"BOOK {book}")
        print(sep)
        print(header)
        print(sep)
        book_words = 0
        for label, wc, pages in groups[book]:
            print(f"{book:<8} {label:<42} {wc:>10,} {pages:>8.1f}")
            book_words += wc
        book_pages = book_words / 250.0
        print(sep)
        print(f"{'SUBTOTAL':<8} {'':<42} {book_words:>10,} {book_pages:>8.1f}")
        print()

    print("MANUSCRIPT TOTALS")
    print(sep)
    print(f"{'ALL':<8} {'':<42} {total_words:>10,} {total_pages:>8.1f}")
    print()

    print("COMPLETION")
    print(sep)
    for name, target in targets:
        print(f"  {name:>6} target : {pct_bar(total_words / target)}")
    print()


if __name__ == "__main__":
    main()
