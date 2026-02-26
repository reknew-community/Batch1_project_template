from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users_by_vendor(db: Session, vendor_id: int):
    return db.query(User).filter(User.vendor_id == vendor_id).all()