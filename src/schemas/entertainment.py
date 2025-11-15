from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class EntertainmentCreate(BaseModel):
    city_id: int
    event_name: str
    event_time: datetime
    duration: str
    address: str


class EntertainmentUpdate(BaseModel):
    city_id: int
    event_name: str
    event_time: datetime
    duration: str
    address: str


class EntertainmentResponse(BaseModel):
    entertainment_id: int
    city_id: int
    event_name: str
    event_time: datetime
    duration: str
    address: str

    class Config:
        orm_mode = True


class EntertainmentsResponse(BaseModel):
    entertainments: list[EntertainmentResponse]