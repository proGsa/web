from __future__ import annotations

from pydantic import BaseModel


class DirectoryRouteCreate(BaseModel):
    type_transport: str
    cost: int
    distance: int
    departure_city: int
    destination_city: int


class DirectoryRouteUpdate(BaseModel):
    type_transport: str | None = None
    cost: int | None = None
    distance: int | None = None
    departure_city: int | None = None
    destination_city: int | None = None


class DirectoryRoutePartialUpdate(BaseModel):
    type_transport: str | None = None


class DirectoryRouteResponse(BaseModel):
    id: int
    type_transport: str
    cost: int
    distance: int
    departure_city: int
    destination_city: int

    class Config:
        orm_mode = True


class DirectoryRouteResponseOut(BaseModel):
    id: int
    type_transport: str
    cost: int
    distance: int
    departure_city: str
    destination_city: str


class DirectoryRoutesResponse(BaseModel):
    d_routes: list[DirectoryRouteResponseOut]