def dates_overlap(a_start, a_end, b_start, b_end):
    return not (a_end < b_start or b_end < a_start)

def detect_conflicts(pilot, drone, mission):
    issues = []

    if not mission.required_skills.issubset(pilot.skills):
        issues.append("Skill mismatch")

    if drone and drone.status.lower() == "maintenance":
        issues.append("Drone in maintenance")

    if pilot.location != mission.location:
        issues.append("Pilot location mismatch")

    for m in pilot.current_assignments:
        if dates_overlap(m.start_date, m.end_date, mission.start_date, mission.end_date):
            issues.append("Pilot double booked")

    return issues
