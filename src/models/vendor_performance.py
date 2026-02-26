from sqlalchemy import Column, BigInteger, String, Integer, DECIMAL, Date, ForeignKey
from src.database import Base

class VendorPerformanceDB(Base):
    __tablename__ = "vendor_performance"

    id = Column(BigInteger, primary_key=True, index=True)

    vendor_id = Column(BigInteger, ForeignKey("vendors.id"), nullable=False)

    calculated_date = Column(Date, nullable=False)
    period_type = Column(String(50), nullable=False)

    total_trips = Column(Integer)
    completed_trips = Column(Integer)
    cancelled_trips = Column(Integer)

    ontime_pickups = Column(Integer)
    ontime_pickup_rate = Column(DECIMAL(10, 4))

    ontime_deliveries = Column(Integer)
    ontime_delivery_rate = Column(DECIMAL(10, 4))

    total_exceptions = Column(Integer)
    exception_rate = Column(DECIMAL(10, 4))

    avg_cost_per_kg = Column(DECIMAL(12, 4))
    avg_cost_per_trip = Column(DECIMAL(12, 4))
    avg_capacity_utilization_pct = Column(DECIMAL(10, 2))

    performance_score = Column(DECIMAL(10, 4))

    created_ts = Column(String(50), nullable=False)
    updated_ts = Column(String(50), nullable=False)