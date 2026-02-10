from agent.intents import parse_intent
from services.sheets_service import read_all_pilots, update_pilot_status

def handle_message(message):
    intent = parse_intent(message)

    if intent == "QUERY_PILOTS":
        pilots = read_all_pilots()
        available = [p["name"] for p in pilots if p.get("status", "").lower() == "available"]
        return {"available_pilots": available}

    if intent == "UPDATE_PILOT":
        parts = message.split()
        pilot_name = parts[-2]
        new_status = parts[-1]
        success = update_pilot_status(pilot_name, new_status)
        return {"updated": success, "pilot": pilot_name, "status": new_status}

    if intent == "URGENT":
        return {"message": "Urgent reassignment engine triggered. See Decision Log for logic."}

    return {"message": "Sorry, I could not understand your request."}
