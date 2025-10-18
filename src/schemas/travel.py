from __future__ import annotations

from pydantic import BaseModel
from typing import List, Optional


class TravelCreate(BaseModel):
    status: str
    user_ids: List[int]
    entertainment_ids: List[int]
    accommodation_ids: List[int]


class TravelUpdate(BaseModel):
    status: Optional[str] = None
    user_ids: Optional[List[int]] = None
    entertainment_ids: Optional[List[int]] = None
    accommodation_ids: Optional[List[int]] = None


class TravelResponse(BaseModel):
    id: int
    status: str
    user_ids: List[int]
    entertainment_ids: List[int]
    accommodation_ids: List[int]

    class Config:
        orm_mode = True

class TravelsResponse(BaseModel):
    travels: List[TravelResponse]

class InsertCityRequest(BaseModel):   
    after_city_id: int 
    transport: str 