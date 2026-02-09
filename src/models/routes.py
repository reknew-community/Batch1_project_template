from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from datetime import datetime
from src.database import Base

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    route_code = Column(String(50), unique=True, nullable=False)
    route_name = Column(String(120), nullable=False)
    origin_city = Column(String(80), nullable=False)
    destination_city = Column(String(80), nullable=False)
    distance_km = Column(Float, nullable=False)
    estimated_hours = Column(Float, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_ts = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_ts = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)