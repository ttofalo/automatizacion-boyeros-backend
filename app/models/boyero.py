from pydantic import BaseModel
from typing import Optional

class BoyeroBase(BaseModel):
    name: str
    gpio_pin: int
    esp_id: str

class BoyeroCreate(BoyeroBase):
    pass

class BoyeroStateUpdate(BaseModel):
    is_on: bool

class BoyeroUpdate(BaseModel):
    name: Optional[str] = None
    gpio_pin: Optional[int] = None
    esp_id: Optional[str] = None
    is_on: Optional[bool] = None

class Boyero(BoyeroBase):
    id: int
    is_on: bool = False

    class Config:
        from_attributes = True
