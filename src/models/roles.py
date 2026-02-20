from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)

    role_name = Column(String(50), nullable=False)
    role_code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))

    permissions = Column(JSON)
    is_system_role = Column(Boolean, default=False)

    created_ts = Column(DateTime, server_default=func.now())
    updated_ts = Column(DateTime, server_default=func.now(), onupdate=func.now())


    users = relationship(
        "User",
        back_populates="role",
        cascade="all, delete"
    )
