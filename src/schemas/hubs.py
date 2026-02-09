from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class HubCreate(BaseModel):
    hub_code: str
    hub_name: str
    hub_type: str
    city: str
    state: str
    pincode: str
    manager_name: Optional[str] = None
    manager_phone: Optional[str] = None
    is_active: bool = True


class HubUpdate(BaseModel):
    hub_name: Optional[str] = None
    hub_type: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    manager_name: Optional[str] = None
    manager_phone: Optional[str] = None
    is_active: Optional[bool] = None


class HubOut(HubCreate):
    id: int
    created_ts: datetime
    updated_ts: datetime

    class Config:
        from_attributes = True