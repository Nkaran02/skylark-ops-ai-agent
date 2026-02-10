def parse_intent(message: str):
    msg = message.lower()

    if "available pilot" in msg:
        return "QUERY_PILOTS"
    if "update pilot" in msg:
        return "UPDATE_PILOT"
    if "urgent" in msg:
        return "URGENT"
    if "conflict" in msg:
        return "CONFLICTS"
    if "assign" in msg:
        return "ASSIGN"

    return "UNKNOWN"
