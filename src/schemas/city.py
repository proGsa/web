from __future__ import annotations

from pydantic import BaseModel


class CityCreate(BaseModel):
    name: str


class CityUpdate(BaseModel):
    name: str


class CityResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CitiesResponse(BaseModel):
    cities: list[CityResponse]
