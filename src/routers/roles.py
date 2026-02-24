from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from src.database import get_db
from src.models.roles import Role
from src.schemas.roles import RoleCreate, RoleUpdate, RoleResponse

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

# Create
@router.post("/", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    existing_role = db.query(Role).filter(Role.role_code == role.role_code).first()
    if existing_role:
        raise HTTPException(status_code=400, detail="Role code already exists")
    db_role = Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

# Read all
@router.get("/", response_model=List[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()

# Read one
@router.get("/{role_id}", response_model=RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).get(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

# Update
@router.put("/{role_id}", response_model=RoleResponse)
def update_role(role_id: int, role_update: RoleUpdate, db: Session = Depends(get_db)):
    role = db.query(Role).get(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    for key, value in role_update.dict(exclude_unset=True).items():
        setattr(role, key, value)
    role.updated_ts = datetime.utcnow()
    db.commit()
    db.refresh(role)
    return role

# Delete
@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).get(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    db.delete(role)
    db.commit()
    return {"detail": "Role deleted successfully"}