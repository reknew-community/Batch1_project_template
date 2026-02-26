from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class TripCreate(BaseModel):
    trip_code: str
    vendor_id: int

    vehicle_number: Optional[str] = None
    driver_name: Optional[str] = None
    driver_phone: Optional[str] = None

    origin_city: str
    destination_city: str
    distance_km: Optional[float] = None

    scheduled_departure: datetime
    scheduled_arrival: datetime
    actual_departure: Optional[datetime] = None
    actual_arrival: Optional[datetime] = None

    vehicle_capacity_kg: Optional[float] = None
    actual_load_kg: Optional[float] = None
    number_of_shipments: Optional[int] = None

    status: Optional[str] = None
    is_ontime_pickup: Optional[bool] = None
    is_ontime_delivery: Optional[bool] = None
    delay_minutes: Optional[int] = None

    has_exception: Optional[bool] = False
    exception_type: Optional[str] = None

    created_ts: str
    updated_ts: str


class TripOut(TripCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int