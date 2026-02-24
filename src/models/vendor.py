from sqlalchemy import Column, String, Boolean, DateTime, BigInteger, DECIMAL, Integer
from sqlalchemy.sql import func
from src.database import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(BigInteger, primary_key=True, index=True)
    vendor_code = Column(String(50), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    vendor_type = Column(String(50))
    contact_person = Column(String(150))
    email = Column(String(150))
    phone = Column(String(20))
    city = Column(String(100))
    state = Column(String(100))
    pricing_model = Column(String(50))
    base_rate = Column(DECIMAL(10, 2))
    total_capacity = Column(Integer)
    available_capacity = Column(Integer)
    service_areas = Column(String(50))
    is_active = Column(Boolean, default=True)
    created_ts = Column(DateTime, server_default=func.now())
    updated_ts = Column(DateTime, server_default=func.now(), onupdate=func.now())
    address = Column(String(255))
    country = Column(String(100))