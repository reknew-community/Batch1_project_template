from pydantic import BaseModel
from typing import Optional

class AwbCreate(BaseModel):
    awb_number: str
    customer_id: int
    booking_id: int
    status: str
    generated_ts: str
    assigned_ts: Optional[str] = None
    used_at: Optional[str] = None

class Awb(AwbCreate):
    id: int

    class Config:
        from_attributes = True  # allows returning SQLAlchemy objects directly