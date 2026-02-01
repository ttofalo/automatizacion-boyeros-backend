from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Optional
from app.services.websocket_manager import manager

router = APIRouter()

@router.websocket("/boyeros")
async def websocket_endpoint(websocket: WebSocket, boyero_id: Optional[int] = None):
    """
    WebSocket endpoint for real-time updates.
    Connect to this endpoint to receive broadcast events when a Boyero state changes.
    URL: ws://<host>:<port>/ws/boyeros?boyero_id=<id> (Optional filter)
    """
    await manager.connect(websocket, boyero_id)
    try:
        while True:
            # Just keep the connection open and listen for messages (even if we don't process them yet)
            # This allows the client to stay connected.
            data = await websocket.receive_text()
            # Optionally echo back or process commands
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket, boyero_id)
        # await manager.broadcast(f"Client left")
