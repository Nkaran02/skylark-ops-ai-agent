import pandas as pd
from  core.models import Pilot, Drone, Mission

def load_pilots(csv_path):
    df = pd.read_csv(csv_path)
    pilots = []

    for _, r in df.iterrows():
        pilots.append(
            Pilot(
                r["name"],
                r["skills"].split(","),
                r["certifications"].split(","),
                r["current location"],
                r["status"]
            )
        )
    return pilots

def load_drones(csv_path):
    df = pd.read_csv(csv_path)
    drones = []

    for _, r in df.iterrows():
        drones.append(
            Drone(
                r["drone id"],
                r["model"],
                r["capabilities"].split(","),
                r["status"],
                r["location"],
                r.get("maintenance due", "")
            )
        )
    return drones

def load_missions(csv_path):
    df = pd.read_csv(csv_path)
    missions = []

    for _, r in df.iterrows():
        missions.append(
            Mission(
                r["project id"],
                r["required skills"].split(","),
                r["location"],
                r["start date"],
                r["end date"],
                r["priority"]
            )
        )
    return missions

