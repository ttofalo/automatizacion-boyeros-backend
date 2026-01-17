from pydantic import BaseModel

class BoyeroBase(BaseModel):
    name: str
    gpio_pin: int
    esp_id: str

class BoyeroCreate(BoyeroBase):
    pass

class BoyeroStateUpdate(BaseModel):
    is_on: bool

class Boyero(BoyeroBase):
    id: int
    is_on: bool = False

    class Config:
        from_attributes = True
