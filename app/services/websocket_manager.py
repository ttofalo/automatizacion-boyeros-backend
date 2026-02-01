from typing import List, Dict, Optional
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        # Global connections (receive all updates)
        self.active_connections: List[WebSocket] = []
        # Specific connections (receive updates only for specific boyero_id)
        self.boyero_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, boyero_id: Optional[int] = None):
        await websocket.accept()
        if boyero_id is not None:
            if boyero_id not in self.boyero_connections:
                self.boyero_connections[boyero_id] = []
            self.boyero_connections[boyero_id].append(websocket)
        else:
            self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket, boyero_id: Optional[int] = None):
        if boyero_id is not None:
            if boyero_id in self.boyero_connections:
                if websocket in self.boyero_connections[boyero_id]:
                    self.boyero_connections[boyero_id].remove(websocket)
                if not self.boyero_connections[boyero_id]:
                    del self.boyero_connections[boyero_id]
        else:
            if websocket in self.active_connections:
                self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def broadcast_json(self, data: dict):
        # Broadcast to global listeners
        for connection in self.active_connections:
            try:
                await connection.send_json(data)
            except Exception as e:
                # Handle potential disconnection errors during broadcast if needed
                print(f"Error broadcasting to client: {e}")
                pass
        
        # Broadcast to specific listeners if applicable
        boyero_id = data.get("id")
        if boyero_id is not None and boyero_id in self.boyero_connections:
            for connection in self.boyero_connections[boyero_id]:
                try:
                    await connection.send_json(data)
                except Exception as e:
                    print(f"Error broadcasting to specific client: {e}")
                    pass

manager = ConnectionManager()
