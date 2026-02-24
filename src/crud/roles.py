from sqlalchemy.orm import Session
from src.models.roles import Role
from src.schemas.roles import RoleCreate, RoleUpdate


def get_roles(db: Session):
    return db.query(Role).all()


def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()


def create_role(db: Session, role: RoleCreate):
    db_role = Role(**role.model_dump())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def update_role(db: Session, db_role: Role, role_update: RoleUpdate):
    for key, value in role_update.model_dump(exclude_unset=True).items():
        setattr(db_role, key, value)

    db.commit()
    db.refresh(db_role)
    return db_role


def deactivate_role(db: Session, db_role: Role):
    db_role.is_active = False
    db.commit()
    db.refresh(db_role)
    return db_role