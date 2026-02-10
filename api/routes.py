from fastapi import APIRouter
from agent.agent import handle_message
from services.sheets_service import update_pilot_status, update_drone_status

router = APIRouter()

@router.post("/agent/chat")
def chat(payload: dict):
    message = payload.get("message", "")
    return handle_message(message)

@router.post("/pilots/update-status")
def update_pilot(payload: dict):
    return {
        "success": update_pilot_status(payload["name"], payload["status"])
    }

@router.post("/drones/update-status")
def update_drone(payload: dict):
    return {
        "success": update_drone_status(payload["drone_id"], payload["status"])
    }
