from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.state_service import StateService
from app.models.boyero import Boyero
from app.models.esp import ESP32, ESP32Create
from typing import List

router = APIRouter()

@router.post("/", response_model=ESP32)
def create_esp(esp: ESP32Create, db: Session = Depends(get_db)):
    """
    Register a new ESP32.
    """
    service = StateService(db)
    # Check if exists first? Service create_esp implicitly might fail if ID exists depending on DB, but SQLAlchemy might just insert.
    # Ideally check existence. For simplicity, just try create.
    # Ideally check existence. For simplicity, just try create.
    return service.create_esp(esp)

@router.get("/", response_model=List[ESP32])
def get_esps(db: Session = Depends(get_db)):
    """
    Get all ESP32s.
    """
    service = StateService(db)
    return service.get_esps()

@router.get("/{esp_id}", response_model=ESP32)
def get_esp(esp_id: str, db: Session = Depends(get_db)):
    """
    Get ESP32 details.
    """
    service = StateService(db)
    esp = service.get_esp(esp_id)
    if not esp:
        raise HTTPException(status_code=404, detail="ESP32 not found")
    return esp

@router.delete("/{esp_id}")
def delete_esp(esp_id: str, db: Session = Depends(get_db)):
    """
    Delete an ESP32.
    """
    service = StateService(db)
    deleted = service.delete_esp(esp_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="ESP32 not found")
    return {"message": "ESP32 deleted"}

@router.get("/{esp_id}/estado", response_model=List[Boyero])
def get_esp_state(esp_id: str, db: Session = Depends(get_db)):
    """
    Endpoint for ESP32 to poll configuration/state.
    Returns list of boyeros assigned to this ESP.
    """
    service = StateService(db)
    # Validate ESP exists?
    esp = service.get_esp(esp_id)
    if not esp:
        raise HTTPException(status_code=404, detail="ESP32 not found")
    return service.get_esp_boyeros(esp_id)
