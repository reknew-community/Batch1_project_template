from sqlalchemy import Column, Integer, String, Date, DateTime, Float
from datetime import datetime
from src.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    booking_number = Column(String(50), unique=True, nullable=False)
    customer_id = Column(Integer, nullable=False)  # other team table later
    booking_date = Column(Date, nullable=False)
    pickup_date = Column(Date, nullable=True)
    total_shipments = Column(Integer, nullable=False, default=0)
    total_weight_kg = Column(Float, nullable=False, default=0.0)
    total_boxes = Column(Integer, nullable=False, default=0)
    status = Column(String(40), nullable=False)
    created_ts = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_ts = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)