from pydantic import BaseModel
from typing import Optional

class ShipmentCreate(BaseModel):
    awb_id: int
    customer_id: int
    booking_id: int

    origin_city: Optional[str] = None
    destination_city: Optional[str] = None
    weight_kg: Optional[float] = None
    current_status: Optional[str] = None

class Shipment(ShipmentCreate):
    id: int

    class Config:
        from_attributes = True