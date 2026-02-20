from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional


class BookingCreate(BaseModel):
    booking_number: str
    customer_id: int
    booking_date: date
    pickup_date: Optional[date] = None
    total_shipments: int = Field(ge=0)
    total_weight_kg: float = Field(ge=0)
    total_boxes: int = Field(ge=0)
    status: str


class BookingUpdate(BaseModel):
    pickup_date: Optional[date] = None
    total_shipments: Optional[int] = Field(default=None, ge=0)
    total_weight_kg: Optional[float] = Field(default=None, ge=0)
    total_boxes: Optional[int] = Field(default=None, ge=0)
    status: Optional[str] = None


class BookingOut(BookingCreate):
    id: int
    created_ts: datetime
    updated_ts: datetime

    class Config:
        from_attributes = True