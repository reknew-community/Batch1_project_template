from sqlalchemy import Column, BigInteger, String, Integer, DateTime
from sqlalchemy.sql import func
from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    full_name = Column(String(150))
    phone = Column(String(20))
    is_active = Column(Integer, default=1)
    role = Column(String(50))
    created_ts = Column(DateTime, server_default=func.now())
    updated_ts = Column(DateTime, onupdate=func.now())