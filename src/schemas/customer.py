from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# -------------------------
# Base
# -------------------------
class CustomerBase(BaseModel):
    customer_code: str
    name: str

    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    country: Optional[str] = None

    credit_rating: Optional[str] = None
    is_active: bool = True


# -------------------------
# Create
# -------------------------
class CustomerCreate(CustomerBase):
    pass


# -------------------------
# Update
# -------------------------
class CustomerUpdate(BaseModel):
    customer_code: Optional[str] = None
    name: Optional[str] = None

    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    country: Optional[str] = None

    credit_rating: Optional[str] = None
    is_active: Optional[bool] = None


# -------------------------
# Response
# -------------------------
class CustomerResponse(CustomerBase):
    id: int
    created_ts: Optional[datetime] = None
    updated_ts: Optional[datetime] = None

    class Config:
        from_attributes = True

