from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(50), unique=True, nullable=False)
    role_code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    is_system_role = Column(Boolean, default=False)

    # # Relationship with User
    # users = relationship("User", back_populates="role")