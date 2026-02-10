# def parse_intent(message: str):
#     msg = message.lower()

#     if "available pilot" in msg:
#         return "QUERY_PILOTS"
#     if "update pilot" in msg:
#         return "UPDATE_PILOT"
#     if "urgent" in msg:
#         return "URGENT"
#     if "conflict" in msg:
#         return "CONFLICTS"
#     if "assign" in msg:
#         return "ASSIGN"

#     return "UNKNOWN"

# PREDEFINED_QUERIES = {
#     "available_pilots": [
#         "show available pilots",
#         "list pilots",
#         "which pilots are available",
#         "free pilots",
#         "available crew"
#     ],
#     "available_drones": [
#         "available drones",
#         "which drones are available",
#         "free drones",
#         "list drones"
#     ],
#     "check_conflicts": [
#         "check conflicts",
#         "any conflicts",
#         "mission conflicts",
#         "schedule conflicts"
#     ],
#     "urgent_reassignment": [
#         "urgent reassignment",
#         "reassign now",
#         "emergency reassignment",
#         "urgent mission"
#     ],
#     "pilot_status": [
#         "pilot status",
#         "show pilot status",
#         "pilot availability"
#     ],
#     "drone_status": [
#         "drone status",
#         "show drone status",
#         "drone availability"
#     ]
# }


# def normalize(text: str) -> str:
#     return text.lower().strip()


# # Enterprise-style intent catalog
# INTENT_PHRASES = {
#     "QUERY_PILOTS": [
#         "available pilot",
#         "available pilots",
#         "show available pilots",
#         "list pilots",
#         "which pilots are available",
#         "free pilots",
#         "pilot availability"
#     ],

#     "UPDATE_PILOT": [
#         "update pilot",
#         "change pilot status",
#         "set pilot status",
#         "mark pilot"
#     ],

#     "URGENT": [
#         "urgent",
#         "urgent reassignment",
#         "emergency",
#         "emergency mission",
#         "urgent mission"
#     ],

#     "CONFLICTS": [
#         "conflict",
#         "check conflicts",
#         "any conflicts",
#         "mission conflicts",
#         "schedule conflicts"
#     ],

#     "ASSIGN": [
#         "assign",
#         "assign pilot",
#         "assign drone",
#         "new assignment"
#     ],

#     "DRONE_STATUS": [
#         "drone status",
#         "available drones",
#         "which drones are available",
#         "free drones",
#         "list drones"
#     ]
# }


# def parse_intent(message: str) -> str:
#     msg = normalize(message)

#     for intent, phrases in INTENT_PHRASES.items():
#         for phrase in phrases:
#             if phrase in msg:
#                 return intent

#     return "UNKNOWN"


def parse_intent(message: str):
    msg = message.lower().strip()

    # --- Predefined Query Matching ---
    for intent, phrases in PREDEFINED_QUERIES.items():
        for phrase in phrases:
            if phrase in msg:
                return intent.upper()

    # --- Fallback keyword logic ---
    if "pilot" in msg and "available" in msg:
        return "AVAILABLE_PILOTS"
    if "drone" in msg:
        return "AVAILABLE_DRONES"
    if "conflict" in msg:
        return "CHECK_CONFLICTS"
    if "urgent" in msg or "emergency" in msg:
        return "URGENT_REASSIGNMENT"
    if "assign" in msg:
        return "ASSIGN"
    if "update pilot" in msg or "change pilot" in msg:
        return "UPDATE_PILOT"

    return "UNKNOWN"


# ---- Predefined Enterprise Queries ----
PREDEFINED_QUERIES = {
    "AVAILABLE_PILOTS": [
        "show available pilots",
        "list pilots",
        "which pilots are available",
        "free pilots",
        "available crew",
        "pilot availability"
    ],
    "AVAILABLE_DRONES": [
        "available drones",
        "which drones are available",
        "free drones",
        "list drones",
        "drone status",
        "drone availability"
    ],
    "CHECK_CONFLICTS": [
        "check conflicts",
        "any conflicts",
        "mission conflicts",
        "schedule conflicts"
    ],
    "URGENT_REASSIGNMENT": [
        "urgent reassignment",
        "reassign now",
        "emergency reassignment",
        "urgent mission",
        "emergency mission"
    ],
    "UPDATE_PILOT": [
        "update pilot",
        "change pilot status",
        "set pilot status"
    ],
    "ASSIGN": [
        "assign pilot",
        "assign drone",
        "new assignment"
    ]
}
