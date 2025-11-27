from __future__ import annotations

from pydantic import BaseModel


class TravelCreate(BaseModel):
    status: str
    user_ids: list[int]
    entertainment_ids: list[int]
    accommodation_ids: list[int]


class TravelUpdate(BaseModel):
    status: str | None = None
    user_ids: list[int] | None = None
    entertainment_ids: list[int] | None = None
    accommodation_ids: list[int] | None = None


class TravelResponse(BaseModel):
    id: int
    status: str
    user_ids: list[int]
    entertainment_ids: list[int]
    accommodation_ids: list[int]

    class Config:
        orm_mode = True


class TravelsResponse(BaseModel):
    travels: list[TravelResponse]


class InsertCityRequest(BaseModel):   
    after_city_id: int 
    transport: str 