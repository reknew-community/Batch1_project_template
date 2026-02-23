from pydantic import BaseModel
from typing import Optional, List, Dict, Union
from datetime import datetime


# -------------------------
# Base
# -------------------------
class RoleBase(BaseModel):
    role_name: str
    role_code: str
    description: Optional[str] = None
    permissions: Optional[Union[List[str], Dict[str, bool]]] = None
    is_system_role: bool = False


# -------------------------
# Create
# -------------------------
class RoleCreate(RoleBase):
    pass


# -------------------------
# Update
# -------------------------
class RoleUpdate(BaseModel):
    role_name: Optional[str] = None
    role_code: Optional[str] = None
    description: Optional[str] = None
    permissions: Optional[Union[List[str], Dict[str, bool]]] = None
    is_system_role: Optional[bool] = None


# -------------------------
# Response
# -------------------------
class RoleResponse(RoleBase):
    id: int
    created_ts: Optional[datetime] = None
    updated_ts: Optional[datetime] = None

    class Config:
        from_attributes = True