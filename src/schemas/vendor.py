from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ----------- CREATE -----------
class VendorCreate(BaseModel):
    vendor_code: str
    name: str
    vendor_type: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pricing_model: Optional[str] = None
    base_rate: Optional[float] = None
    total_capacity: Optional[int] = None
    available_capacity: Optional[int] = None
    service_areas: Optional[str] = None
    address: Optional[str] = None
    country: Optional[str] = None
    is_active: Optional[bool] = True


# ----------- UPDATE -----------
class VendorUpdate(BaseModel):
    name: Optional[str] = None
    vendor_type: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pricing_model: Optional[str] = None
    base_rate: Optional[float] = None
    total_capacity: Optional[int] = None
    available_capacity: Optional[int] = None
    service_areas: Optional[str] = None
    address: Optional[str] = None
    country: Optional[str] = None
    is_active: Optional[bool] = None


# ----------- RESPONSE -----------
class VendorResponse(BaseModel):
    id: int
    vendor_code: str
    name: str
    vendor_type: Optional[str]
    contact_person: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    city: Optional[str]
    state: Optional[str]
    pricing_model: Optional[str]
    base_rate: Optional[float]
    total_capacity: Optional[int]
    available_capacity: Optional[int]
    service_areas: Optional[str]
    is_active: bool
    created_ts: datetime
    updated_ts: datetime
    address: Optional[str]
    country: Optional[str]

    class Config:
        from_attributes = True