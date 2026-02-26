from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime

class VendorPerformanceCreate(BaseModel):
    vendor_id: int
    calculated_date: date
    period_type: str

    total_trips: Optional[int] = None
    completed_trips: Optional[int] = None
    cancelled_trips: Optional[int] = None

    ontime_pickups: Optional[int] = None
    ontime_pickup_rate: Optional[float] = None

    ontime_deliveries: Optional[int] = None
    ontime_delivery_rate: Optional[float] = None

    total_exceptions: Optional[int] = None
    exception_rate: Optional[float] = None

    avg_cost_per_kg: Optional[float] = None
    avg_cost_per_trip: Optional[float] = None
    avg_capacity_utilization_pct: Optional[float] = None

    performance_score: Optional[float] = None

    created_ts: Optional[datetime] = None
    updated_ts: Optional[datetime] = None


class VendorPerformanceOut(VendorPerformanceCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int