# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ClinicFlow
import os, re


def merge_imports(src_path):
    with open(src_path) as f:
        src = f.read()
    lines = [l for l in src.splitlines() if l.strip().startswith("import ")]
    merged = []
    seen = set()
    for ln in lines:
        m = re.match(r"import\s+(.+)", ln)
        if not m: continue
        names = m.group(1).split(",")
        new_names = []
        for n in names:
            if n.strip() not in seen:
                new_names.append(n.strip())
                seen.add(n.strip())
        merged.append(f"import {', '.join(new_names)}\n")
    return "\n".join(merged), len(lines) - len(merged)


if __name__ == "__main__":
    print("clinicflow.import_merging: ready")
