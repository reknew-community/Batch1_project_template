from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# -------------------------
# Base
# -------------------------
class VendorBase(BaseModel):
    name: str
    vendor_code: Optional[str] = None
    vendor_type: Optional[str] = None
    contact_person: Optional[str] = None

    email: Optional[str] = None
    phone: Optional[str] = None

    city: Optional[str] = None
    state: Optional[str] = None

    service_areas: Optional[list] = None
    pricing_model: Optional[str] = None

    base_rate: Optional[float] = None
    total_capacity: Optional[int] = None
    available_capacity: Optional[int] = None

    is_active: bool = True


# -------------------------
# Create
# -------------------------
class VendorCreate(VendorBase):
    pass


# -------------------------
# Update
# -------------------------
class VendorUpdate(BaseModel):
    name: Optional[str] = None
    vendor_type: Optional[str] = None
    contact_person: Optional[str] = None

    email: Optional[str] = None
    phone: Optional[str] = None

    city: Optional[str] = None
    state: Optional[str] = None

    service_areas: Optional[list] = None
    pricing_model: Optional[str] = None

    base_rate: Optional[float] = None
    total_capacity: Optional[int] = None
    available_capacity: Optional[int] = None

    is_active: Optional[bool] = None


# -------------------------
# Response
# -------------------------
class VendorResponse(VendorBase):
    id: int
    created_ts: datetime
    updated_ts: datetime

    class Config:
        from_attributes = True
