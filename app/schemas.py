from pydantic import BaseModel
from typing import Optional


class Shop(BaseModel):
    name: str
    latitude: float
    longitude: float
    address: str
    city: str


class UpdateShop(BaseModel):
    name: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    address: Optional[str]
    city: Optional[str]
