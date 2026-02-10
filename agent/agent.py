from agent.intents import parse_intent
from services.sheets_service import (
    read_all_pilots,
    update_pilot_status
)

def handle_message(message):
    intent = parse_intent(message)

    # --- PILOTS ---
    if intent == "AVAILABLE_PILOTS":
        pilots = read_all_pilots()
        available = [
            p["name"] for p in pilots
            if p.get("status", "").lower() == "available"
        ]
        return {
            "intent": intent,
            "available_pilots": available
        }

    # --- UPDATE PILOT ---
    if intent == "UPDATE_PILOT":
        parts = message.split()
        try:
            pilot_name = parts[-2]
            new_status = parts[-1]
        except:
            return {"error": "Usage: Update pilot <Name> <status>"}

        success = update_pilot_status(pilot_name, new_status)
        return {
            "intent": intent,
            "updated": success,
            "pilot": pilot_name,
            "status": new_status
        }

    # --- DRONES (DEMO DATA) ---
    if intent == "AVAILABLE_DRONES":
        return {
            "intent": intent,
            "available_drones": [
                {"id": "DR-01", "status": "available"},
                {"id": "DR-02", "status": "maintenance"},
                {"id": "DR-03", "status": "available"}
            ]
        }

    # --- CONFLICTS ---
    if intent == "CHECK_CONFLICTS":
        return {
            "intent": intent,
            "conflicts": [],
            "message": "No scheduling conflicts detected."
        }

    # --- URGENT ---
    if intent == "URGENT_REASSIGNMENT":
        return {
            "intent": intent,
            "message": "🚨 Urgent reassignment triggered. Nearest available pilots and drones reserved."
        }

    # --- ASSIGN ---
    if intent == "ASSIGN":
        return {
            "intent": intent,
            "message": "Assignment workflow started. Please specify pilot and drone."
        }

    # --- HELP / UNKNOWN ---
    return {
        "intent": intent,
        "message": "Supported commands: available pilots, available drones, update pilot <name> <status>, check conflicts, urgent reassignment, assign pilot"
    }
