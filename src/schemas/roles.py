from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


# -------------------------
# Base
# -------------------------
class RoleBase(BaseModel):
    role_name: str
    role_code: str
    description: Optional[str] = None
    permissions: Optional[Dict[str, bool]] = None
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
    permissions: Optional[Dict[str, bool]] = None
    is_system_role: Optional[bool] = None


# -------------------------
# Response
# -------------------------
from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class RoleResponse(BaseModel):
    id: int
    role_name: str
    role_code: str
    description: Optional[str]
    permissions: Optional[Any]   
    is_system_role: bool
    created_ts: datetime
    updated_ts: datetime

    class Config:
        from_attributes = True

