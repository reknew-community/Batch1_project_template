from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class RouteCreate(BaseModel):
    route_code: str
    route_name: str
    origin_city: str
    destination_city: str
    distance_km: float = Field(gt=0)
    estimated_hours: float = Field(gt=0)
    is_active: bool = True


class RouteUpdate(BaseModel):
    route_name: Optional[str] = None
    origin_city: Optional[str] = None
    destination_city: Optional[str] = None
    distance_km: Optional[float] = Field(default=None, gt=0)
    estimated_hours: Optional[float] = Field(default=None, gt=0)
    is_active: Optional[bool] = None


class RouteOut(RouteCreate):
    id: int
    created_ts: datetime
    updated_ts: datetime

    class Config:
        from_attributes = True