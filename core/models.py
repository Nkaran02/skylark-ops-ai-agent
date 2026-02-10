class Pilot:
    def __init__(self, name, skills, certifications, location, status):
        self.name = name
        self.skills = set(map(str.strip, skills))
        self.certifications = set(map(str.strip, certifications))
        self.location = location
        self.status = status
        self.current_assignments = []

class Drone:
    def __init__(self, drone_id, model, capabilities, status, location, maintenance_due):
        self.drone_id = drone_id
        self.model = model
        self.capabilities = set(map(str.strip, capabilities))
        self.status = status
        self.location = location
        self.maintenance_due = maintenance_due
        self.current_assignment = None

class Mission:
    def __init__(self, project_id, required_skills, location, start_date, end_date, priority):
        self.project_id = project_id
        self.required_skills = set(map(str.strip, required_skills))
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.priority = int(priority)
