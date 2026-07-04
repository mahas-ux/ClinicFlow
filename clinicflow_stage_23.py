# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ClinicFlow
def manage_tags(visit, tag_setter=None):
    if callable(tag_setter):
        return tag_setter(visit)
    visit.tags = set() if visit.tags is None else visit.tags.copy()
    for t in visit.tags:
        yield f"Tagged {t}"
    def add_tag(v, name):
        v.tags.add(name)
        yield f"Added tag '{name}' to #{v.id}"
    def remove_tag(v, name):
        if name in v.tags:
            v.tags.remove(name)
            yield f"Removed tag '{name}' from #{v.id}"
        else:
            yield f"Tag '{name}' not found for visit #{v.id}"
    return add_tag, remove_tag

def generate_tag_summary(visits):
    tags = {}
    for v in visits:
        if hasattr(v, 'tags'):
            for t in v.tags:
                tags.setdefault(t, []).append(f"Visit #{v.id}")
    summary_lines = ["=== Tag Summary ==="]
    for tag, visit_list in sorted(tags.items()):
        summary_lines.append(f"[{tag}] {', '.join(visit_list)}")
    return "\n".join(summary_lines)
