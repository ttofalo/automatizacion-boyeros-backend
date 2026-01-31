from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.state_service import StateService
from app.models.boyero import Boyero, BoyeroStateUpdate, BoyeroCreate, BoyeroUpdate
from app.services.websocket_manager import manager
from typing import List, Optional

router = APIRouter()

@router.get("/", response_model=List[Boyero])
def read_boyeros(id: Optional[int] = None, db: Session = Depends(get_db)):
    """
    Get all boyeros.
    """
    service = StateService(db)
    return service.get_boyeros(id=id)

@router.patch("/{boyero_id}/estado", response_model=Boyero)
def change_boyero_state(boyero_id: int, state: BoyeroStateUpdate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Change the state of a specific boyero (ON/OFF).
    """
    service = StateService(db)
    updated = service.update_boyero_state(boyero_id, state.is_on)
    if not updated:
        raise HTTPException(status_code=404, detail="Boyero not found")
    
    # Broadcast update
    # Convert DB model to Pydantic model then to dict to ensure serialization
    boyero_data = Boyero.model_validate(updated).model_dump()
    background_tasks.add_task(manager.broadcast_json, boyero_data)
    
    return updated

@router.put("/{boyero_id}", response_model=Boyero)
def update_boyero(boyero_id: int, boyero_update: BoyeroUpdate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Update Boyero details.
    """
    service = StateService(db)
    updated = service.update_boyero(boyero_id, boyero_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Boyero not found")
        
    # Broadcast update
    boyero_data = Boyero.model_validate(updated).model_dump()
    background_tasks.add_task(manager.broadcast_json, boyero_data)
    
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
