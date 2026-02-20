from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.roles import RoleCreate, RoleUpdate, RoleResponse
from app.crud.roles import (
    get_roles,
    get_role_by_id,
    create_role,
    update_role,
    deactivate_role
)

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

# -----------------------------
# GET – All roles
# -----------------------------
@router.get("/", response_model=List[RoleResponse])
def read_roles(db: Session = Depends(get_db)):
    return get_roles(db)


# -----------------------------
# POST – Create role
# -----------------------------
@router.post(
    "/",
    response_model=RoleResponse,
    status_code=status.HTTP_201_CREATED
)
def create(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)


# -----------------------------
# GET – Single role
# -----------------------------
@router.get("/{role_id}", response_model=RoleResponse)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


# -----------------------------
# PUT – Update role
# -----------------------------
@router.put("/{role_id}", response_model=RoleResponse)
def update(
    role_id: int,
    role_update: RoleUpdate,
    db: Session = Depends(get_db)
):
    role = get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    return update_role(db, role, role_update)


# -----------------------------
# DELETE – Delete role
# -----------------------------

@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    db_role = get_role_by_id(db, role_id)
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")

    deactivate_role(db, db_role)
    return {"message": "Role deactivated successfully"}
