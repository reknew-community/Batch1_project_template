from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from src.database import Base

class Hub(Base):
    __tablename__ = "hubs"

    id = Column(Integer, primary_key=True, index=True)
    hub_code = Column(String(50), unique=True, nullable=False)
    hub_name = Column(String(120), nullable=False)
    hub_type = Column(String(50), nullable=False)
    city = Column(String(80), nullable=False)
    state = Column(String(80), nullable=False)
    pincode = Column(String(20), nullable=False)
    manager_name = Column(String(120), nullable=True)
    manager_phone = Column(String(30), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_ts = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_ts = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)