wordcount:
    python3 scripts/wordcount.py

wc: wordcount

build-context:
    python3 scripts/build_context_zip.py
    @echo "Context package written to dist/"
