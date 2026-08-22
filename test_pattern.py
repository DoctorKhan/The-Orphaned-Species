import re

sentences = [
    "It has a stamp and a date and his parents' names under it, and he can't get his hands around any of it at once.",
    "He holds the paper. The stamp is wet. The date is before he was born, or close enough.",
    "Maren fastened the button he had missed, then held her palm against his sternum until he looked at her.",
    "The door and the window and the wall were all shut.",
    "The river does the remembering for him.",
    "Heat climbs Eli's neck.",
    "Babaji split your name off theirs so anyone looking for them would not find you here. Orphan on paper.",
    "He walks to the table and picks up the paper and opens it.",
    "stamp and date and names",
    "a stamp and a date and his parents",
]

# Tightened pattern: determiner-led noun phrases joined by 'and'
PARALLEL_ABSTRACTION = re.compile(
    r"\b(?:the|a|an|his|her|their)\s+[a-z]+(?:\s+[a-z]+)?\b(?:\s+and\s+(?:the|a|an|his|her|their)\s+[a-z]+(?:\s+[a-z]+)?){2,}",
    re.IGNORECASE,
)

for s in sentences:
    hits = PARALLEL_ABSTRACTION.findall(s)
    print(f"MATCH: {len(hits)} => {hits[:1]}")
