# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ClinicFlow
def recommend_priority(visit):
    """Simple scoring for visit priority based on clinical urgency and wait time."""
    score = 0
    if visit.priority == 'critical': score += 10
    elif visit.priority == 'high': score += 7
    elif visit.priority == 'medium': score += 4
    elif visit.priority == 'low': score += 1

    if visit.wait_minutes > 60: score += 3
    if visit.wait_minutes > 30: score += 2

    if visit.symptoms and any(s in visit.symptoms for s in ['chest pain', 'breathing difficulty', 'stroke symptoms']):
        score += 15

    return score
