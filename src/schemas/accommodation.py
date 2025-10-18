from __future__ import annotations
from datetime import datetime
from pydantic import BaseModel
from typing import List


class AccommodationCreate(BaseModel):
    name: str
    city_id: int
    address: str
    price: float
    type: str
    rating: int | None = None
    check_in: datetime
    check_out: datetime


class AccommodationUpdate(BaseModel):
    name: str
    city_id: int
    address: str
    price: float
    type: str
    rating: int | None = None
    check_in: datetime
    check_out: datetime


class AccommodationResponse(BaseModel):
    accommodation_id: int
    name: str
    city_id: int
    address: str
    price: float
    type: str
    rating: int | None = None
    check_in: datetime
    check_out: datetime

    class Config:
        orm_mode = True


class AccommodationsResponse(BaseModel):
    accommodations: List[AccommodationResponse]
