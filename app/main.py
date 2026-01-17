from fastapi import FastAPI
from app.routers import esp, boyeros
from app.core.config import settings
from app.db.database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(esp.router, prefix="/esp", tags=["esp"])
app.include_router(boyeros.router, prefix="/boyeros", tags=["boyeros"])

@app.get("/")
def root():
    return {"message": "Boyeros Backend API running"}

