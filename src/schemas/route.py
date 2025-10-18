from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class RouteCreate(BaseModel):
    d_route_id: int
    travel_id: int
    start_time: datetime
    end_time: datetime
    type: str 


class RouteUpdate(BaseModel):
    d_route_id: Optional[int] = None
    travel_id: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    type: Optional[str] = None


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
    routes: List[RouteResponse]