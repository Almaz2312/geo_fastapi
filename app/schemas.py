from pydantic import BaseModel
from typing import Optional


class Shop(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    address: str
    city: str


class UpdateShop(BaseModel):
    id: Optional[int]
    name: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    address: Optional[str]
    city: Optional[str]
