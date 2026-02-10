def find_preemption_candidates(mission, pilots):
    candidates = []

    for pilot in pilots:
        for assigned in pilot.current_assignments:
            if assigned.priority < mission.priority:
                candidates.append({
                    "pilot": pilot.name,
                    "current_mission": assigned.project_id,
                    "priority_gap": mission.priority - assigned.priority
                })

    return sorted(candidates, key=lambda x: x["priority_gap"], reverse=True)
