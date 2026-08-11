#!/usr/bin/env python3
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parent.parent

# Only the canonical manuscript location counts toward completion.
# ROOT/"manuscripts"/book_i_chapters is legacy/duplicate content (an early
# chapter split of I_The_Breach.md) and would double-count Book I if included.
MANUSCRIPT_ROOTS = [
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


def parse_args():
    parser = argparse.ArgumentParser(description="Manuscript word/page/completion report.")
    parser.add_argument(
        "--target", type=int, default=120_000,
        help="Generic per-volume word-count target for the % column (default: 120,000).",
    )
    parser.add_argument(
        "--no-detail", action="store_true",
        help="Skip the per-file breakdown and only print the summary table.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    files = collect_manuscripts()
    if not files:
        print("No manuscript files found.")
        return

    rows = []
    for path, wc in files:
        label = label_for(path)
        book = book_group(label)
        pages = wc / 250.0
        rows.append((book, label, wc, pages))

    # Group by book
    groups = {}
    order = []
    for book, label, wc, pages in rows:
        groups.setdefault(book, []).append((label, wc, pages))
        if book not in order:
            order.append(book)

    header = f"{'Book':<8} {'File':<42} {'Words':>10} {'Pages':>8}"
    sep = "─" * 74

    book_totals = {}
    if not args.no_detail:
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
            book_totals[book] = book_words
            book_pages = book_words / 250.0
            print(sep)
            print(f"{'SUBTOTAL':<8} {'':<42} {book_words:>10,} {book_pages:>8.1f}")
            print()
    else:
        for book in order:
            book_totals[book] = sum(wc for _, wc, _ in groups[book])

    total_words = sum(book_totals.values())
    total_pages = total_words / 250.0

    # Book I is the project's own density-parity reference (99_active_todo.md
    # § "II-IV density parity"), separate from a generic trade-novel target.
    parity_words = book_totals.get("I")

    print("COMPLETION — by book")
    print(sep)
    label_w = 28
    print(
        f"{'Book':<{label_w}}{'Words':>8}{'Pages':>8}"
        f"{f'% of {args.target // 1000}k':>12}"
        + (f"{'% of Book I':>13}" if parity_words else "")
    )
    print(sep)
    for book in order:
        wc = book_totals[book]
        pages = wc / 250.0
        pct_target = wc / args.target * 100
        line = f"{book:<{label_w}}{wc:>8,}{pages:>8.0f}{pct_target:>11.1f}%"
        if parity_words:
            pct_parity = wc / parity_words * 100
            line += f"{pct_parity:>12.1f}%"
        print(line)
    print(sep)
    line = f"{'Total':<{label_w}}{total_words:>8,}{total_pages:>8.0f}"
    print(line)
    print()


if __name__ == "__main__":
    main()
