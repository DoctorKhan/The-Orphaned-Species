#!/usr/bin/env python3
"""
Generate prose audits for each manuscript chapter.
Applies the cadence / AI-pattern checklist from `14_literary_speculative_thriller_style_guide.md`
and the anti-cadence rules from `AGENTS.md` prose discipline.

Outputs `*_prose_audit.md` alongside the manuscripts.

Usage:
    python3 scripts/generate_prose_audit.py
"""

from __future__ import annotations

import re
from pathlib import Path
from collections import Counter

BASE = Path(__file__).resolve().parent.parent
MANUSCRIPTS = BASE / "manuscripts"
OUT = MANUSCRIPTS

BOOKS = [
    {
        "key": "I",
        "title": "Volume I — *The Breach* — Prose Audit",
        "manuscript": "I_The_Breach.md",
        "audit_file": "I_The_Breach_prose_audit.md",
    },
    {
        "key": "II",
        "title": "Volume II — *The Descent* — Prose Audit",
        "manuscript": "II_The_Descent.md",
        "audit_file": "II_The_Descent_prose_audit.md",
    },
    {
        "key": "III",
        "title": "Volume III — *The Compact* — Prose Audit",
        "manuscript": "III_The_Compact.md",
        "audit_file": "III_The_Compact_prose_audit.md",
    },
    {
        "key": "IV",
        "title": "Volume IV — *The Court of Threads* — Prose Audit",
        "manuscript": "IV_The_Court_of_Threads.md",
        "audit_file": "IV_The_Court_of_Threads_prose_audit.md",
    },
]

# ---------------------------------------------------------------------------
# Pattern sets (kept short and compilable)
# ---------------------------------------------------------------------------

NOT_X_BUT_Y = re.compile(r"\bnot\b[^.\n]{0,30}\bbut\b", re.IGNORECASE)
STACKED_EM_DASHES = re.compile(r"—.*?—.*?—", re.DOTALL)
COLON_HEAVY = re.compile(r":[^:\n]{0,40}:[^:\n]{0,40}:")

TELL_NOT_SHOW = re.compile(
    r"\b(?:which\s+meant|in\s+other\s+words|that\s+is\s+to\s+say|in\s+effect|in\s+fact|in\s+reality|in\s+essence|really|actually|basically|essentially|simply|just|merely|only)\b",
    re.IGNORECASE,
)

# Echo-closer approximation: final sentence of a section/chapter that lands on
# thematic nouns without image or verb change.
ECHO_CLOSER = re.compile(
    r"(?:the\s+(?:meaning|truth|point|lesson|moral|heart|essence|core|secret|gift|price|cost)\s+(?:of|was|were|is|are|had been))\b[^.\n]{0,80}\.",
    re.IGNORECASE,
)

ABSTRACT_TERMS = re.compile(
    r"\b(?:obligation|debt|procedure|failure|success|fear|truth|meaning|love|hate|anger|grief|cost|promise|burden|weight|absence|loss|gain|power|authority|control|rebellion|surrender|renunciation|sacrifice|redemption|salvation|damnation|divinity|humanity|nature|identity|memory|forgetting|recognition|refusal|acceptance|rejection|willingness|reluctance)\b",
    re.IGNORECASE,
)

BODY_NOUNS = re.compile(
    r"\b(?:hand|foot|eye|ear|mouth|throat|chest|shoulder|back|knee|skin|bone|blood|breath|finger|toe|hair|sweat|tear|salt|water|fire|ash|mud|stone|wood|iron|glass|dust|soil|root|leaf|branch|flower|fruit|seed|grain|rice|clay|copper|bronze|gold|steel|wire|cable|circuit|board|screen|light|dark|shadow|sun|moon|star|rain|wind|cold|heat|sound|silence|voice|word|name|ring|tablet|book|page|door|wall|floor|roof|road|path|bridge|vessel|cup|bowl|plate|knife|blade|gun|bullet|paper|pen|ink|stain|scar|wound|bruise|burn|cut|mark|tattoo|veil|cloth|thread|rope|cord|chain|lock|key|pass|ticket|stamp|seal|wax|sign|token|object|thing|piece|shard|fragment|bit|remains|trace|track|step|footprint|print|streak|line|dot|hole|crack|split|break|tear|knot|loop|spiral|arch|curve|angle|corner|edge|side|face|surface|depth|body)\b",
    re.IGNORECASE,
)

ABSTRACT_OPEN = re.compile(
    r"^(?:It\s+(?:was|is)\s+(?:clear|obvious|evident|apparent|true|certain)\s+that|"
    r"What\s+(?:Eli|Wren|Somchai|Rowan|Maren|Lang|Sol|Qiao|Sora|Shireen|Dara|Hassan|Babaji|Rasel)\s+(?:knew|understood|realized|saw|felt)\s+was|"
    r"The\s+(?:truth|reality|fact|secret|meaning|point|lesson|problem|question|cost|price)\s+was|"
    r"What\s+(?:mattered|counted|stuck|remained)\s+was|"
    r"None\s+of\s+this\s+was\s+(?:new|real|true|the\s+point)|"
    r"All\s+of\s+this\s+was\s+(?:familiar|known|old|unnecessary|beside\s+the\s+point)|"
    r"This\s+was\s+(?:not|never)\s+(?:the\s+point|what\s+mattered|what\s+counted)|"
    r"What\s+(?:Eli|Wren|Somchai|Rowan|Maren|Lang|Sol|Qiao|Sora|Shireen|Dara|Hassan|Babaji|Rasel)\s+(?:didn't|did)\s+know\s+was)",
    re.IGNORECASE,
)

STALE_FRAMING = {
    "Rasel recovered": "Rasel refused; stays by choice",
    "recover Rasel": "Rasel refused; stays by choice",
    "Eli recovers Rasel": "Eli refuses Rasel",
    "Rasel instrument antagonist": "Rasel off-page by choice",
    "Rasel present": "Rasel off-page by choice",
    "father alive": "father left behind / refused",
    "Rasel stays": "Rasel refuses",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def split_chapters(text: str):
    chapters = []
    lines = text.split("\n")
    current_start = 0
    current_title = None
    for i, line in enumerate(lines):
        if re.match(r"^## Chapter", line):
            if current_title is not None:
                chapters.append((current_start, i, current_title))
            current_start = i
            current_title = line.strip()
    if current_title is not None:
        chapters.append((current_start, len(lines), current_title))
    return chapters


def windowed_counts(text: str, window: int = 220) -> tuple[int, int, int]:
    """Return max co-occurrence pressure of abstract vs body nouns in any window.

    We scan a sliding window of characters and count abstract-term and body-noun
    hits inside it.  The heuristic flag fires when the worst-case abstract count
    materially outpaces body nouns.
    """
    abstract_hits = [(m.start(), m.end()) for m in ABSTRACT_TERMS.finditer(text)]
    body_hits = [(m.start(), m.end()) for m in BODY_NOUNS.finditer(text)]

    if not abstract_hits:
        return 0, 0, 0

    best = 0
    best_body = 0
    best_start = 0
    j = 0
    for i, (start, _) in enumerate(abstract_hits):
        while j < len(body_hits) and body_hits[j][1] < start:
            j += 1
        k = j
        body = 0
        while k < len(body_hits) and body_hits[k][0] <= start + window:
            body += 1
            k += 1
        if i + 1 > best:
            best = i + 1
            best_body = body
            best_start = start
    return best, best_body, best_start


def audit_chapter(title: str, body: str, lines: list[str]) -> dict:
    text = "\n".join(lines)
    flags = []
    metrics = {}

    # Length metrics
    metrics["word_count"] = len(text.split())
    metrics["sentence_count"] = max(1, len(re.findall(r"[.!?]+", text)))

    # Pattern checks
    not_x_but_y = NOT_X_BUT_Y.findall(text)
    if not_x_but_y:
        flags.append(f"NOT-X-BUT-Y ({len(not_x_but_y)} hits)")

    stacked_em = STACKED_EM_DASHES.findall(text)
    if stacked_em:
        flags.append(f"STACKED-EM-DASHES ({len(stacked_em)} hits)")

    colon_heavy = COLON_HEAVY.findall(text)
    if colon_heavy:
        flags.append(f"COLON-HEAVY ({len(colon_heavy)} hits)")

    echo_closers = ECHO_CLOSER.findall(text)
    if echo_closers:
        flags.append(f"ECHO-CLOSER ({len(echo_closers)} hits)")

    tell_not_show = TELL_NOT_SHOW.findall(text)
    if tell_not_show:
        flags.append(f"TELL-NOT-SHOW ({len(tell_not_show)} hits)")

    # Abstract/body balance
    abstract_total = len(ABSTRACT_TERMS.findall(text))
    body_total = len(BODY_NOUNS.findall(text))
    if abstract_total > 20:
        flags.append(f"ABSTRACT-DENSE ({abstract_total} abstract terms, {body_total} body terms)")

    worst_abstract, worst_body, _ = windowed_counts(text)
    if worst_abstract >= 4 and worst_body < worst_abstract:
        flags.append(
            f"ABSTRACT-OVER-BODY (windowed {worst_abstract} abstract vs {worst_body} body)"
        )

    # Chapter open check
    para_match = re.search(r"\n\n(.+?)(?:\n\n|\Z)", text, re.DOTALL)
    if para_match:
        first_para = para_match.group(1)
        words = first_para.split()
        if len(words) > 20 and ABSTRACT_OPEN.search(first_para):
            flags.append("ABSTRACT-OPEN")
        elif len(words) > 20 and not BODY_NOUNS.search(first_para):
            flags.append("OPEN-LIGHT-ON-BODY")

    # Stale framing
    stale_hits = []
    for phrase, _replacement in STALE_FRAMING.items():
        if phrase.lower() in text.lower():
            stale_hits.append(phrase)
    if stale_hits:
        flags.append(f"STALE-FRAMING ({len(stale_hits)} phrases)")

    return {
        "title": title,
        "metrics": metrics,
        "flags": flags,
    }


def generate_audit(book_cfg):
    manuscript_path = MANUSCRIPTS / book_cfg["manuscript"]
    audit_path = OUT / book_cfg["audit_file"]

    text = manuscript_path.read_text()
    chapters = split_chapters(text)
    lines = text.split("\n")

    chapter_audits = []
    for start, end, title in chapters:
        chapter_lines = lines[start:end]
        audit = audit_chapter(title, "", chapter_lines)
        chapter_audits.append(audit)

    # Aggregate summary
    flag_counter = Counter()
    for a in chapter_audits:
        for f in a["flags"]:
            flag_counter[f.split(" (")[0]] += 1

    md = []
    md.append(f"# {book_cfg['title']}")
    md.append("*Generated from on-disk files. Rerun after prose revisions.*\n")
    md.append("> **Generated:** current as of last script run.")
    md.append("> Treat as draft until manual review.\n")

    md.append("## Summary")
    total_flags = sum(len(a["flags"]) for a in chapter_audits)
    flagged_chapters = sum(1 for a in chapter_audits if a["flags"])
    md.append(f"- **Chapters audited:** {len(chapter_audits)}")
    md.append(f"- **Flagged chapters:** {flagged_chapters}")
    md.append(f"- **Total flag instances:** {total_flags}")
    md.append("")

    if flag_counter:
        md.append("| Flag | Chapters |")
        md.append("|---|---|")
        for name, count in flag_counter.most_common():
            md.append(f"| {name} | {count} |")
        md.append("")

    md.append("## Chapter-level detail")
    md.append("")
    for audit in chapter_audits:
        md.append(f"### {audit['title']}")
        md.append(f"- **Word count:** {audit['metrics']['word_count']}")
        md.append(f"- **Sentence count:** {audit['metrics']['sentence_count']}")
        if audit["flags"]:
            md.append("- **Flags:**")
            for f in audit["flags"]:
                md.append(f"  - {f}")
        else:
            md.append("- **Flags:** none")
        md.append("")

    md.append("## Open items")
    md.append("")
    md.append("1. These are heuristic flags, not verdicts. Review flagged passages individually.")
    md.append("2. `ABSTRACT-OVER-BODY` uses a sliding window; tune the window size if false-positive rate is high.")
    md.append("3. `STALE-FRAMING` is pattern-based; expand `STALE_FRAMING` after each lock change.")
    md.append("4. `ABSTRACT-OPEN` / `OPEN-LIGHT-ON-BODY` check the first paragraph only.")
    md.append("")
    md.append("## Methodology")
    md.append("")
    md.append("Pattern checks applied:")
    md.append("- `NOT-X-BUT-Y`: default contrastive shape")
    md.append("- `STACKED-EM-DASHES`: 2+ em dashes in one sentence")
    md.append("- `COLON-HEAVY`: 2+ colons in one sentence")
    md.append("- `ECHO-CLOSER`: final-sentence thematic restatement")
    md.append("- `TELL-NOT-SHOW`: interpretive-telling words")
    md.append("- `ABSTRACT-DENSE`: high abstract-noun count")
    md.append("- `ABSTRACT-OVER-BODY`: abstract terms outweigh body terms in a local window")
    md.append("- `ABSTRACT-OPEN` / `OPEN-LIGHT-ON-BODY`: chapter open without physical body")
    md.append("- `STALE-FRAMING`: superseded canonical phrasing")
    md.append("")
    md.append("Source: `14_literary_speculative_thriller_style_guide.md` § *Generic-cadence / AI-pattern checklist* and § *Human-prose lock*; `AGENTS.md` prose discipline.")

    audit_path.write_text("\n".join(md))
    return str(audit_path)


def main():
    generated = []
    for book_cfg in BOOKS:
        path = generate_audit(book_cfg)
        generated.append(path)
        print(f"Generated: {path}")
    print(f"\n{len(generated)} prose audits generated.")


if __name__ == "__main__":
    main()
