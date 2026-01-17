from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.state_service import StateService
from app.models.boyero import Boyero, BoyeroStateUpdate, BoyeroCreate
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Boyero])
def read_boyeros(db: Session = Depends(get_db)):
    """
    Get all boyeros.
    """
    service = StateService(db)
    return service.get_boyeros()

@router.patch("/{boyero_id}/estado", response_model=Boyero)
def change_boyero_state(boyero_id: int, state: BoyeroStateUpdate, db: Session = Depends(get_db)):
    """
    Change the state of a specific boyero (ON/OFF).
    """
    service = StateService(db)
    updated = service.update_boyero_state(boyero_id, state.is_on)
    if not updated:
        raise HTTPException(status_code=404, detail="Boyero not found")
    return updated

@router.post("/", response_model=Boyero)
def create_boyero(boyero: BoyeroCreate, db: Session = Depends(get_db)):
    """
    Create a new boyero (Helper for setup).
    """
    service = StateService(db)
    return service.create_boyero(boyero)

@router.delete("/{boyero_id}")
def delete_boyero(boyero_id: int, db: Session = Depends(get_db)):
    """
    Delete a boyero.
    """
    service = StateService(db)
    deleted = service.delete_boyero(boyero_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Boyero not found")
    return {"message": "Boyero deleted"}
