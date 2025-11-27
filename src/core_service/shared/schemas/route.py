from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class RouteCreate(BaseModel):
    d_route_id: int
    travel_id: int
    start_time: datetime
    end_time: datetime
    type: str 


class RouteUpdate(BaseModel):
    d_route_id: int | None = None
    travel_id: int | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    type: str | None = None


class RouteResponse(BaseModel):
    route_id: int
    d_route_id: int
    travel_id: int
    start_time: datetime
    end_time: datetime
    type: str

    class Config:
        orm_mode = True


class InsertCityRequest(BaseModel):  
    after_city_id: int 
    transport: str 


class RoutesResponse(BaseModel):
    routes: list[RouteResponse]