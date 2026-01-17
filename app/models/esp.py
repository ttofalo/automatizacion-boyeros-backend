from pydantic import BaseModel

class ESP32Base(BaseModel):
    name: str
    active: bool = True

class ESP32Create(ESP32Base):
    id: str # MAC Address or Unique ID

class ESP32(ESP32Base):
    id: str

    class Config:
        from_attributes = True
