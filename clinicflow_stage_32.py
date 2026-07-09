# === Stage 32: Add pagination helpers for long console output ===
# Project: ClinicFlow
def paginate(text, chunk=80):
    """Break a long string into fixed-width chunks for console output."""
    if len(text) <= chunk:
        yield text
        return
    start = 0
    while start < len(text):
        end = min(start + chunk, len(text))
        yield text[start:end]
        start = end

def paginate_with_marker(text, chunk=80, marker="..."):
    """Paginate with a truncation marker if the last chunk is incomplete."""
    chunks = list(paginate(text, chunk))
    if len(chunks) > 1 and len(chunks[-1]) < chunk:
        chunks[-1] = marker + " " + chunks[-1]
    yield from chunks
