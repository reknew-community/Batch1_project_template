from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# -------------------------
# Base
# -------------------------
class UserBase(BaseModel):
    username: str
    email: EmailStr

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None

    role_id: int
    customer_id: Optional[int] = None
    vendor_id: Optional[int] = None

    is_active: bool = True
    email_verified: bool = False


# -------------------------
# Create
# -------------------------
class UserCreate(UserBase):
    password: str


# -------------------------
# Update
# -------------------------
class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None

    role_id: Optional[int] = None
    customer_id: Optional[int] = None
    vendor_id: Optional[int] = None

    is_active: Optional[bool] = None


# -------------------------
# Response
# -------------------------
class UserResponse(UserBase):
    id: int
    last_login: Optional[datetime] = None
    created_ts: datetime
    updated_ts: datetime

    class Config:
        from_attributes = True
