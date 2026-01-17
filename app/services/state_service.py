from sqlalchemy.orm import Session
from app.db.models import DBBoyero, DBESP32
from app.models.boyero import BoyeroCreate, BoyeroStateUpdate, Boyero
from app.models.esp import ESP32Create, ESP32
from typing import List, Optional

class StateService:
    def __init__(self, db: Session):
        self.db = db

    def get_boyeros(self) -> List[DBBoyero]:
        return self.db.query(DBBoyero).all()

    def get_boyero(self, boyero_id: int) -> Optional[DBBoyero]:
        return self.db.query(DBBoyero).filter(DBBoyero.id == boyero_id).first()

    def update_boyero_state(self, boyero_id: int, is_on: bool) -> Optional[DBBoyero]:
        boyero = self.get_boyero(boyero_id)
        if boyero:
            boyero.is_on = is_on
            self.db.commit()
            self.db.refresh(boyero)
        return boyero

    def create_boyero(self, boyero: BoyeroCreate) -> DBBoyero:
        db_boyero = DBBoyero(
            name=boyero.name,
            gpio_pin=boyero.gpio_pin,
            esp_id=boyero.esp_id,
            is_on=False
        )
        self.db.add(db_boyero)
        self.db.commit()
        self.db.refresh(db_boyero)
        return db_boyero

    def delete_boyero(self, boyero_id: int) -> bool:
        boyero = self.get_boyero(boyero_id)
        if boyero:
            self.db.delete(boyero)
            self.db.commit()
            return True
        return False

        return False

    # ESP Methods
    def get_esps(self) -> List[DBESP32]:
        return self.db.query(DBESP32).all()

    def get_esp_boyeros(self, esp_id: str) -> List[DBBoyero]:
        return self.db.query(DBBoyero).filter(DBBoyero.esp_id == esp_id).all()
    
    def get_esp(self, esp_id: str) -> Optional[DBESP32]:
        return self.db.query(DBESP32).filter(DBESP32.id == esp_id).first()

    def create_esp(self, esp: ESP32Create) -> DBESP32:
        db_esp = DBESP32(id=esp.id, name=esp.name, active=esp.active)
        self.db.add(db_esp)
        self.db.commit()
        self.db.refresh(db_esp)
        return db_esp

    def delete_esp(self, esp_id: str) -> bool:
        esp = self.get_esp(esp_id)
        if esp:
            self.db.delete(esp)
            self.db.commit()
            return True
        return False
