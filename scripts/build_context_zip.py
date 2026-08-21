#!/usr/bin/env python3
"""Build a comprehensive, deterministic context zip for AI-assisted review.

Creates: dist/orphaned-species-context-<YYYYMMDD-HHMMSS>.zip

Contents:
- AGENTS.md / project agent instructions
- World bible, timeline, series structure
- Layer 1 manuscripts + prose audits
- Beatsheets, architecture, locks, planning docs
- Companion / concept books from Books/ and symlinked Layer 2 titles
- Active draft fragments
- A manifest with word counts per included file
"""

from __future__ import annotations

import argparse
import io
import os
import re
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

EXCLUDE_DIRS = {
    ".git",
    "node_modules",
    "venv",
    ".venv",
    "__pycache__",
    "dist",
    "build",
    ".claude",
    ".windsurf",
}

EXCLUDE_FILES = {
    ".DS_Store",
    "audit_temp_findings.json",
    "README.md",
}

EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".pdf",
    ".bin",
    ".zip",
    ".bak",
}

# Source roots and their preferred archive prefix.
SOURCE_ROOTS: list[tuple[Path, str]] = [
    (ROOT, "00_ROOT"),
    (ROOT / "50_The_Orphaned_Species" / "manuscripts", "01_MANUSCRIPTS"),
    (ROOT / "50_The_Orphaned_Species" / "manuscripts", "02_MANUSCRIPT_AUDITS"),
    (ROOT / "50_The_Orphaned_Species", "03_PLANNING"),
    (ROOT / "Books", "04_BOOKS"),
    (ROOT / "Books" / "Manual_Override", "04_BOOKS_Manual_Override"),
    (ROOT / "Books" / "The_Social_Game", "04_BOOKS_The_Social_Game"),
    (ROOT / "Books" / "The_Human_Experiment", "04_BOOKS_The_Human_Experiment"),
    (ROOT / "Books" / "The_Cosmic_Game", "04_BOOKS_The_Cosmic_Game"),
]

# Symlinked Layer 2 companion titles at repo root.
SYMLINK_COMPANIONS: dict[str, str] = {
    "10_Manual_Override": "04_BOOKS_Manual_Override",
    "20_The_Social_Game": "04_BOOKS_The_Social_Game",
    "30_The_Human_Experiment": "04_BOOKS_The_Human_Experiment",
    "40_The_Consciousness_Technologies": "04_BOOKS_The_Cosmic_Game",
}

# Active draft fragments at repo root.
ACTIVE_DRAFTS = [Path("tmp_ch2_part1.md"), Path("tmp_ch2_section1.md"), Path("tmp_ch2_section2.md")]

# Explicit root docs to include under 00_ROOT.
ROOT_DOCS = [
    Path("AGENTS.md"),
    Path("CLAUDE.md"),
    Path("GEMINI.md"),
    Path("SERIES_STRUCTURE.md"),
    Path("WORLD_BIBLE.md"),
    Path("PROJECT_HISTORY.md"),
    Path("BOOK_IV_REVIEW.md"),
    Path("charkha-craft-lock.md"),
    Path("50_The_Orphaned_Species/14_literary_speculative_thriller_style_guide.md"),
]

MANIFEST_NAME = "CONTEXT_MANIFEST.txt"
README_NAME = "README_CONTEXT.txt"


@dataclass(frozen=True)
class FileEntry:
    arcname: str
    content: str
    size: int


def relsafe(path: Path) -> Path:
    try:
        return path.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return path.relative_to(ROOT)


def is_excluded(path: Path) -> bool:
    if any(part in EXCLUDE_DIRS for part in path.parts):
        return True
    if path.name in EXCLUDE_FILES:
        return True
    if path.suffix.lower() in EXCLUDE_SUFFIXES:
        return True
    if path.is_symlink():
        try:
            resolved = path.resolve()
        except OSError:
            return True
        if not resolved.exists():
            return True
    return False


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def read_file_safe(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None


def collect_root_docs() -> list[FileEntry]:
    entries: list[FileEntry] = []
    for rel in ROOT_DOCS:
        path = ROOT / rel
        text = read_file_safe(path)
        if text is None:
            continue
        entries.append(FileEntry(f"00_ROOT/{rel.name}", text, len(text.encode("utf-8"))))
    return entries


def collect_active_drafts() -> list[FileEntry]:
    entries: list[FileEntry] = []
    for rel in ACTIVE_DRAFTS:
        path = ROOT / rel
        text = read_file_safe(path)
        if text is None:
            continue
        entries.append(FileEntry(f"05_ACTIVE_DRAFTS/{rel.name}", text, len(text.encode("utf-8"))))
    return entries


def collect_tree(root: Path, prefix: str, subdir_filter: str | None = None) -> list[FileEntry]:
    entries: list[FileEntry] = []
    if not root.exists():
        return entries
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if is_excluded(path):
            continue
        if subdir_filter:
            parts = path.relative_to(root).parts
            if parts and parts[0] != subdir_filter:
                continue
        text = read_file_safe(path)
        if text is None:
            continue
        rel = path.relative_to(root)
        arcname = f"{prefix}/{rel.as_posix()}"
        entries.append(FileEntry(arcname, text, len(text.encode("utf-8"))))
    return entries


def collect_companion_books() -> list[FileEntry]:
    entries: list[FileEntry] = []
    for name, prefix in SYMLINK_COMPANIONS.items():
        link = ROOT / name
        if not link.exists() or not link.is_symlink():
            continue
        target = link.resolve()
        if not target.exists():
            continue
        # Include book docs/downloads readable versions if present.
        docs_downloads = target / "docs" / "downloads"
        if docs_downloads.exists():
            for path in sorted(docs_downloads.rglob("*")):
                if not path.is_file() or is_excluded(path):
                    continue
                text = read_file_safe(path)
                if text is None:
                    continue
                arcname = f"{prefix}/docs_downloads/{path.name}"
                entries.append(FileEntry(arcname, text, len(text.encode("utf-8"))))
        # Include src tree if present.
        src = target / "src"
        if src.exists():
            entries.extend(collect_tree(src, prefix))
    return entries


def build_manifest(entries: list[FileEntry]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    total_files = len(entries)
    total_bytes = sum(e.size for e in entries)
    total_words = sum(word_count(e.content) for e in entries)
    lines = [
        f"# Context zip manifest — generated {now}",
        f"Files: {total_files}",
        f"Total bytes: {total_bytes:,}",
        f"Total words (approx): {total_words:,}",
        "",
        "## Included files",
        "",
    ]
    for e in sorted(entries, key=lambda x: x.arcname):
        wc = word_count(e.content)
        lines.append(f"- {e.arcname}  ({wc:,} words, {e.size:,} bytes)")
    lines += [
        "",
        "## Usage note",
        "",
        "This zip is intended for AI-assisted review. AGENTS.md at 00_ROOT/AGENTS.md",
        "contains project instructions and prose/style rules.",
    ]
    return "\n".join(lines) + "\n"


def build_readme() -> str:
    return "\n".join([
        "# Orphaned Species — AI Review Context Package",
        "",
        "This archive contains the project's canonical reference material, manuscripts,",
        "planning documents, and companion concept books for AI-assisted review.",
        "",
        "Start with:",
        "  - 00_ROOT/AGENTS.md",
        "  - 00_ROOT/WORLD_BIBLE.md",
        "  - 00_ROOT/SERIES_STRUCTURE.md",
        "  - 01_MANUSCRIPTS/ for the current novels",
        "  - CONTEXT_MANIFEST.txt for a full file list with word counts",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        "",
    ]) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build comprehensive context zip.")
    parser.add_argument(
        "--out",
        type=str,
        default=None,
        help="Explicit output zip path. Default: dist/orphaned-species-context-<timestamp>.zip",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    DIST.mkdir(exist_ok=True)

    entries: list[FileEntry] = []
    entries.extend(collect_root_docs())
    entries.extend(collect_active_drafts())

    # 01_MANUSCRIPTS: canonical manuscript files only, excluding audits and backups.
    manuscript_dir = ROOT / "50_The_Orphaned_Species" / "manuscripts"
    for path in sorted(manuscript_dir.rglob("*")):
        if not path.is_file() or is_excluded(path):
            continue
        if path.name.endswith("_prose_audit.md") or path.suffix == ".bak":
            continue
        text = read_file_safe(path)
        if text is None:
            continue
        entries.append(
            FileEntry(f"01_MANUSCRIPTS/{path.relative_to(manuscript_dir).as_posix()}", text, len(text.encode("utf-8")))
        )

    # 02_MANUSCRIPT_AUDITS: prose audit files.
    for path in sorted(manuscript_dir.glob("*_prose_audit.md")):
        if is_excluded(path):
            continue
        text = read_file_safe(path)
        if text is None:
            continue
        entries.append(
            FileEntry(f"02_MANUSCRIPT_AUDITS/{path.name}", text, len(text.encode("utf-8")))
        )

    entries.extend(collect_tree(ROOT / "50_The_Orphaned_Species", "03_PLANNING"))
    entries.extend(collect_companion_books())

    manifest = build_manifest(entries)
    readme = build_readme()

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    out_path = Path(args.out) if args.out else DIST / f"orphaned-species-context-{timestamp}.zip"

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(README_NAME, readme)
        zf.writestr(MANIFEST_NAME, manifest)
        for e in sorted(entries, key=lambda x: x.arcname):
            zf.writestr(e.arcname, e.content)

    size_kb = out_path.stat().st_size / 1024
    print(f"Wrote: {out_path}")
    print(f"Files packed: {len(entries)}")
    print(f"Archive size: {size_kb:,.1f} KB")


if __name__ == "__main__":
    main()
