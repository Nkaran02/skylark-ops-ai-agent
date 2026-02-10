def skill_match_score(pilot, mission):
    matched = mission.required_skills.intersection(pilot.skills)
    return len(matched) / max(1, len(mission.required_skills))

def find_best_pilots(pilots, mission):
    scored = []

    for p in pilots:
        if p.status.lower() != "available":
            continue
        score = skill_match_score(p, mission)
        scored.append((p, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored
