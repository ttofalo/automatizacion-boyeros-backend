from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import esp, boyeros, websockets
from app.core.config import settings
from app.db.database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="""
    API Backend for Boyeros Automation.
    
    ## WebSockets
    
    You can connect to the WebSocket endpoint to receive real-time updates when a Boyero changes state.
    
    **Endpoint**: `/ws/boyeros`
    **URL**: `ws://<host>:8000/ws/boyeros`
    
    When a Boyero is updated (via API), the new state object is broadcasted to all connected clients.
    """
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(esp.router, prefix="/esp", tags=["esp"])
app.include_router(boyeros.router, prefix="/boyeros", tags=["boyeros"])
app.include_router(websockets.router, prefix="/ws", tags=["websockets"])

@app.get("/")
def root():
    return {"message": "Boyeros Backend API running"}

