# import gspread
# from google.oauth2.service_account import Credentials
# from sky.config import GOOGLE_SHEET_ID, SERVICE_ACCOUNT_FILE

# SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# def get_client():
#     creds = Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES
#     )
#     return gspread.authorize(creds)

# def get_pilot_sheet():
#     client = get_client()
#     sheet = client.open_by_key(GOOGLE_SHEET_ID)
#     return sheet.worksheet("Pilot Roster")

# def get_drone_sheet():
#     client = get_client()
#     sheet = client.open_by_key(GOOGLE_SHEET_ID)
#     return sheet.worksheet("Drone Fleet")

# def read_all_pilots():
#     ws = get_pilot_sheet()
#     return ws.get_all_records()

# def read_all_drones():
#     ws = get_drone_sheet()
#     return ws.get_all_records()

# def update_pilot_status(pilot_name, new_status):
#     ws = get_pilot_sheet()
#     records = ws.get_all_records()

#     for i, row in enumerate(records, start=2):
#         if row.get("name") == pilot_name:
#             status_col = ws.find("status").col
#             ws.update_cell(i, status_col, new_status)
#             return True
#     return False

# def update_drone_status(drone_id, new_status):
#     ws = get_drone_sheet()
#     records = ws.get_all_records()

#     for i, row in enumerate(records, start=2):
#         if row.get("drone id") == drone_id:
#             status_col = ws.find("status").col
#             ws.update_cell(i, status_col, new_status)
#             return True
#     return False

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


# ---------------------------
# CSV HELPERS
# ---------------------------

def _read_csv(filename):
    path = DATA_DIR / filename
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _write_csv(filename, rows, fieldnames):
    path = DATA_DIR / filename
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------
# READ OPERATIONS
# ---------------------------

def read_all_pilots():
    return _read_csv("pilot_roster.csv")


def read_all_drones():
    return _read_csv("drone_fleet.csv")


def read_all_missions():
    return _read_csv("missions.csv")


# ---------------------------
# WRITE OPERATIONS (SYNC)
# ---------------------------

def update_pilot_status(pilot_name, new_status):
    rows = _read_csv("pilot_roster.csv")

    for r in rows:
        if r.get("name") == pilot_name:
            r["status"] = new_status

    if rows:
        _write_csv("pilot_roster.csv", rows, rows[0].keys())

    return True


def update_drone_status(drone_id, new_status):
    rows = _read_csv("drone_fleet.csv")

    for r in rows:
        # handle different possible column names
        if r.get("drone_id") == drone_id or r.get("id") == drone_id:
            r["status"] = new_status

    if rows:
        _write_csv("drone_fleet.csv", rows, rows[0].keys())

    return True
