from sqlalchemy import (
    Column, BigInteger, String, Integer, Boolean,
    DECIMAL, DateTime, ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.database import Base


class TripDB(Base):
    __tablename__ = "trips"

    id = Column(BigInteger, primary_key=True, index=True)
    trip_code = Column(String(50), unique=True, nullable=False)

    vendor_id = Column(BigInteger, ForeignKey("vendors.id"), nullable=False)

    vehicle_number = Column(String(50))
    driver_name = Column(String(150))
    driver_phone = Column(String(20))

    origin_city = Column(String(100), nullable=False)
    destination_city = Column(String(100), nullable=False)
    distance_km = Column(DECIMAL(10, 2))

    scheduled_departure = Column(DateTime, nullable=False)
    actual_departure = Column(DateTime, nullable=True)
    scheduled_arrival = Column(DateTime, nullable=False)
    actual_arrival = Column(DateTime, nullable=True)

    vehicle_capacity_kg = Column(DECIMAL(10, 2))
    actual_load_kg = Column(DECIMAL(10, 2))
    number_of_shipments = Column(Integer)

    status = Column(String(50))

    is_ontime_pickup = Column(Boolean)
    is_ontime_delivery = Column(Boolean)
    delay_minutes = Column(Integer)

    has_exception = Column(Boolean, default=False)
    exception_type = Column(String(100))

    created_ts = Column(DateTime, server_default=func.now(), nullable=False)
    updated_ts = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    vendor = relationship("Vendor", back_populates="trips")