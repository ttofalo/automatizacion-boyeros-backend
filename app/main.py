from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import esp, boyeros
from app.core.config import settings
from app.db.database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

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

@app.get("/")
def root():
    return {"message": "Boyeros Backend API running"}

