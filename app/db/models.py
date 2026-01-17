from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class DBESP32(Base):
    __tablename__ = "esp32"

    id = Column(String, primary_key=True, index=True) # MAC Address
    name = Column(String)
    active = Column(Boolean, default=True)

    boyeros = relationship("DBBoyero", back_populates="esp")

class DBBoyero(Base):
    __tablename__ = "boyeros"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gpio_pin = Column(Integer)
    is_on = Column(Boolean, default=False)
    esp_id = Column(String, ForeignKey("esp32.id"))

    esp = relationship("DBESP32", back_populates="boyeros")
