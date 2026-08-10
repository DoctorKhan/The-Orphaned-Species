#!/usr/bin/env python3
"""
Density / Reveal / Logic audit for The Orphaned Species Books I-IV.
Reads chapter boundaries, then checks each chapter against locked craft rules.
Outputs structured JSON report.
"""
import re, json, os
from pathlib import Path

BASE = Path("/Users/khan/Projects/The-Orphaned-Species/50_The_Orphaned_Species/manuscripts")
BOOKS = {
    "I": "I_The_Breach.md",
    "II": "II_The_Descent.md",
    "III": "III_The_Compact.md",
    "IV": "IV_The_Court_of_Threads.md",
}

# Locked terms / lore vocabulary that counts as "named concept"
NEW_CONCEPT_PATTERN = re.compile(
    r"\b(?:continuity|attestation|Weaver|Cloister|Thread|Mandate|Charkha|Custodian|Stack|Rootbook|"
    r"Three Circles|Tablet|Apkallu|Igigi|Forks|Bridge|Umul|Loop|Extra|remittance|hierarchy|"
    r"compression cohort|dormant clause|selection mark|route ledger|blue cup|attestation delegate|"
    r"conductor|charged ground|deep-time|ancient face|panspermia|Elvish|Dreamer|Last Dreamers|"
    r"Manual Override|Social Game|Human Experiment|Cosmic Game|witness-language|somatic|"
    r"threshold|Field That Counts|Living Route|Riddling Ground|False Heir|Room Prepared|"
    r"Body of State|Two Houses|Present Consent|Living World|Compact|Cost of Consent|"
    r"Handover|Hearing Begins|Tree with No Top|Human Doors|Forming Line|Two Teams|"
    r"Hour That Belongs|What Came Home|Refusal|Buried Instrument|Healer's Terms|"
    r"What They Took|Changing Map|Bitter Cup|Transmission Station|Release|"
    r"Boat at Morning|Terms of Welcome|Person Freedom Failed|Standard|Names They Carry|"
    r"Crown With an End|Doors|Three Rooms|What We Build|Rumor|Before the First Breath)\b",
    re.IGNORECASE,
)

# Passive discovery / coincidence language to flag
PASSIVE_PATTERN = re.compile(
    r"\b(?:finds?|discovered|discover|accidentally|coincidence|coincidentally|"
    r"by chance|as if by|happens to|just so|luckily|fortuitous|out of nowhere|"
    r"passive reveal|info.?dump|exposition)\b",
    re.IGNORECASE,
)

# Deep-time residue indicators (objects, places, practices, sayings, forms, bodies)
DEEP_TIME_PATTERN = re.compile(
    r"\b(?:tablet|stone|artifact|fossil|ruin|relic|idol|wafer|tree|root|"
    r"body.?memory|rhyme|echo|fossil|residue|ancient|deep.?time|first.?city|"
    r"Eridu|Sanxingdui|Göbekli|Pömmelte|Rollright|Men-an-Tol|Anglesey|Stonehenge|Avebury|"
    r"Malacca|Bali|Albion|Cherry Cube|Forest City|subak|gamelan|"
    r"prayer fragment|medal|chipped enamel|red pen mark|teacher's rod|blue ink|"
    r"route slip|dead credential|knuckle tap|field burn|scarred doorframe|"
    r"three.?ring|Three Circles|chalked line|compression cohort|continuity seat|"
    r"wage ticket|boy on the call sheet|Friday dinner|"
    r"Last Dreamers|dream communion|resistor smoke|lab-floor|lullaby|"
    r"archangel|seventy sons|Igigi|elves|ælf|"
    r"selection mark|disputed thing|continuity cipher|attestation delegate)\b",
    re.IGNORECASE,
)

# Protagonist action indicators
PROTAGONIST_ACTION = re.compile(
    r"\b(?:Eli|Wren|Rowan)\s+(?:chooses?|decides?|acts?|moves?|takes?|gives?|refuses?|"
    r"says?|names?|writes?|reads?|finds?|turns?|walks?|runs?|enters?|leaves?|"
    r"carries?|holds?|opens?|closes?|checks?|asks?|answers?|negotiates?|"
    r"routes?|verifies?|attests?|records?|witnesses?|protects?|defends?|"
    r"refuses?|accepts?|rejects?|names?)\b",
    re.IGNORECASE,
)

# Opponent present-tense job indicators
OPPONENT_JOB = re.compile(
    r"\b(?:Lang|Sol|Henley|Novak|Voss|Selin|Cuno|Maren|Rasel|Maren|"
    r"review|vote|hearing|assessment|inspection|audit|registry|ledger|"
    r"deadline|Thursday|Friday|schedule|closure|quarantine|convoy|escort|"
    r"placement|attestation|recertification|continuity|continuity seat|"
    r"dormant clause|budget|meeting|briefing|report)\b",
    re.IGNORECASE,
)

# Cost indicators
COST_PATTERN = re.compile(
    r"\b(?:cost|price|toll|burn|lose|lost|sacrifice|surrender|compromise|"
    r"ache|wrist ache|pain|injury|burn|shaking|grief|anger|fear|"
    r"private|alone|solo|without|neither|no one|not asking|not telling|"
    r"unannounced|hidden|carry|weight|burden)\b",
    re.IGNORECASE,
)

# Clock A/B indicators (two tensions)
CLOCK_A = re.compile(r"\b(?:rescue|parents|Maren|Rasel|capture|extraction|Hinge|release|reunion|family|home)\b", re.IGNORECASE)
CLOCK_B = re.compile(r"\b(?:network|route|registry|jurisdiction|continuity|vote|review|hearing|attestation|comp|compact|corridor|charter)\b", re.IGNORECASE)

def split_chapters(text):
    """Split text into chapters by ## Chapter headings."""
    chapters = []
    lines = text.split("\n")
    current_start = 0
    current_title = None
    chapter_starts = []
    
    for i, line in enumerate(lines):
        if re.match(r"^## Chapter", line):
            if current_title is not None:
                chapter_starts.append((current_start, i, current_title))
            current_start = i
            current_title = line.strip()
    
    if current_title is not None:
        chapter_starts.append((current_start, len(lines), current_title))
    
    return chapter_starts

def audit_chapter(lines, chapter_title):
    """Run density/reveal/logic checks on a chapter."""
    text = "\n".join(lines)
    words = text.split()
    word_count = len(words)
    
    # Skip very short chapters (< 200 words)
    if word_count < 200:
        return None
    
    # --- DENSITY CHECKS ---
    new_concepts = NEW_CONCEPT_PATTERN.findall(text)
    unique_concepts = set(c.lower() for c in new_concepts)
    term_density = len(unique_concepts)
    
    deep_time_hits = DEEP_TIME_PATTERN.findall(text)
    deep_time_count = len(deep_time_hits)
    
    # Exposition density: count explanatory sentences (sentences with "is/are/was/were" + abstract noun)
    # Rough proxy: sentences with "is" + "the" + abstract noun pattern
    expository_sentences = 0
    sentences = re.split(r'[.!?]+', text)
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 20:
            continue
        # Check for exposition markers
        if re.search(r"\b(?:is|are|was|were)\s+(?:the|a|an)\s+\w+\s+(?:of|to|for|that|which)\b", sent):
            if not re.search(r"\b(?:Eli|Wren|Rowan|he|she|they)\b", sent):
                expository_sentences += 1
    
    # --- REVEAL CHECKS ---
    passive_hits = PASSIVE_PATTERN.findall(text)
    passive_count = len(passive_hits)
    
    # Check for "desire before information": Eli's want appears before lore
    desire_before_info = False
    desire_match = re.search(r"\b(?:wants?|needs?|wishes?|longs?|tries?|seeks?|hopes?)\b.*?\b(?:proof|record|home|family|place|belong|remain|know|find|rescue|release)\b", text, re.IGNORECASE)
    info_match = re.search(r"\b(?:continuity|attestation|Tablet|Rootbook|Three Circles|Charkha|Mandate|Custodian|Igigi|Elvish|Dreamer)\b", text, re.IGNORECASE)
    if desire_match and info_match:
        desire_pos = desire_match.start()
        info_pos = info_match.start()
        desire_before_info = desire_pos < info_pos
    
    # Check for abstract nouns without bodies
    abstract_nouns = re.findall(r"\b(?:the selection mark|the disputed thing|continuity seat|dormant clause|compression cohort|attestation delegate)\b", text, re.IGNORECASE)
    abstract_without_body = len(abstract_nouns)
    
    # Cosmological answers in one chapter
    cosmic_answers = re.findall(r"\b(?:is|are|was|were)\s+(?:the|a|an)\s+(?:Manual Override|Social Game|Human Experiment|Cosmic Game|Tablet of Destinies|Rootbook|Player|robot|Igigi|Elvish|Dreamer)\b", text, re.IGNORECASE)
    cosmic_count = len(cosmic_answers)
    
    # --- LOGIC CHECKS ---
    clock_a = len(CLOCK_A.findall(text))
    clock_b = len(CLOCK_B.findall(text))
    dual_clock = clock_a > 0 and clock_b > 0
    
    protagonist_active = len(PROTAGONIST_ACTION.findall(text))
    
    opponent_present = len(OPPONENT_JOB.findall(text))
    
    cost_present = len(COST_PATTERN.findall(text))
    
    # Check for passive voice in key discovery moments
    passive_voice_in_reveal = False
    reveal_sentences = re.split(r'[.!?]+', text)
    for sent in reveal_sentences:
        if re.search(r"\b(?:was found|was discovered|was revealed|was learned|was known)\b", sent, re.IGNORECASE):
            if re.search(r"\b(?:Eli|Wren|Rowan|he|she)\b", sent, re.IGNORECASE):
                passive_voice_in_reveal = True
                break
    
    # Cost → next chapter: chapter ends with a cost marker
    chapter_ends_with_cost = False
    last_20_lines = "\n".join(lines[-20:]) if len(lines) >= 20 else "\n".join(lines)
    if COST_PATTERN.search(last_20_lines):
        chapter_ends_with_cost = True
    
    return {
        "title": chapter_title,
        "word_count": word_count,
        "density": {
            "term_density": term_density,
            "deep_time_residue": deep_time_count,
            "expository_sentences": expository_sentences,
        },
        "reveal": {
            "passive_discovery_hits": passive_count,
            "desire_before_info": desire_before_info,
            "abstract_without_body": abstract_without_body,
            "cosmic_answers_in_chapter": cosmic_count,
            "passive_voice_in_reveal": passive_voice_in_reveal,
        },
        "logic": {
            "dual_clock": dual_clock,
            "clock_a_hits": clock_a,
            "clock_b_hits": clock_b,
            "protagonist_action_hits": protagonist_active,
            "opponent_job_hits": opponent_present,
            "cost_present": cost_present,
            "ends_with_cost": chapter_ends_with_cost,
        },
        "flags": [],
    }

# Run audit
report = {}
for book, filename in BOOKS.items():
    path = BASE / filename
    text = path.read_text()
    chapters = split_chapters(text)
    book_report = []
    
    for start, end, title in chapters:
        chapter_lines = text.split("\n")[start:end]
        result = audit_chapter(chapter_lines, title)
        if result:
            # Generate flags
            flags = []
            if result["density"]["term_density"] > 8:
                flags.append(f"TERM DENSITY HIGH ({result['density']['term_density']} unique concepts)")
            if result["density"]["deep_time_residue"] == 0:
                flags.append("NO DEEP-TIME RESIDUE")
            if result["density"]["expository_sentences"] > 5:
                flags.append(f"EXPOSITION HEAVY ({result['density']['expository_sentences']} expository sentences)")
            if result["reveal"]["passive_discovery_hits"] > 2:
                flags.append(f"PASSIVE DISCOVERY LANGUAGE ({result['reveal']['passive_discovery_hits']} hits)")
            if not result["reveal"]["desire_before_info"]:
                flags.append("DESIRE BEFORE INFO FAIL")
            if result["reveal"]["abstract_without_body"] > 0:
                flags.append(f"ABSTRACT NOUN WITHOUT BODY ({result['reveal']['abstract_without_body']})")
            if result["reveal"]["cosmic_answers_in_chapter"] > 1:
                flags.append(f"MULTIPLE COSMIC ANSWERS ({result['reveal']['cosmic_answers_in_chapter']})")
            if result["reveal"]["passive_voice_in_reveal"]:
                flags.append("PASSIVE VOICE IN REVEAL")
            if not result["logic"]["dual_clock"]:
                flags.append("NO DUAL CLOCK")
            if result["logic"]["protagonist_action_hits"] < 3:
                flags.append(f"LOW PROTAGONIST ACTION ({result['logic']['protagonist_action_hits']})")
            if result["logic"]["opponent_job_hits"] < 2:
                flags.append(f"WEAK OPPONENT JOB ({result['logic']['opponent_job_hits']})")
            if not result["logic"]["ends_with_cost"]:
                flags.append("NO COST AT CHAPTER END")
            
            result["flags"] = flags
            book_report.append(result)
    
    report[book] = book_report

# Output summary
print("=" * 70)
print("DENSITY / REVEAL / LOGIC AUDIT REPORT")
print("=" * 70)
for book, chapters in report.items():
    print(f"\n### Book {book} — {len(chapters)} chapters audited")
    flagged = [c for c in chapters if c["flags"]]
    clean = [c for c in chapters if not c["flags"]]
    print(f"  Clean: {len(clean)} | Flagged: {len(flagged)}")
    if flagged:
        for c in flagged:
            flags_str = " | ".join(c["flags"])
            print(f"  [{c['title'][:40]}] {flags_str}")

# Save full JSON
out_path = Path("/Users/khan/Projects/The-Orphaned-Species/50_The_Orphaned_Species/audit_density_reveal_logic.json")
out_path.write_text(json.dumps(report, indent=2))
print(f"\nFull report saved to: {out_path}")
