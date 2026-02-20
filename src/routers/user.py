from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.crud.user import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    deactivate_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# -----------------------------
# GET – All users
# -----------------------------
@router.get("/", response_model=List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)


# -----------------------------
# POST – Create user
# -----------------------------
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


# -----------------------------
# PUT – Update user
# -----------------------------
@router.put("/{user_id}", response_model=UserResponse)
def update(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db)
):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return update_user(db, db_user, user_update)


# -----------------------------
# DELETE – Soft delete user
# -----------------------------
@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    deactivate_user(db, db_user)
    return {"message": "User deactivated successfully"}
