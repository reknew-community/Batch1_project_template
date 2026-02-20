from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    TIMESTAMP,
    JSON,
    DECIMAL
)
from sqlalchemy.sql import func
from app.database import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)
    vendor_code = Column(String(150), unique=True, index=True)

    vendor_type = Column(String(50))
    contact_person = Column(String(150))

    email = Column(String(150))
    phone = Column(String(20))

    city = Column(String(100))
    state = Column(String(100))

    service_areas = Column(JSON)
    pricing_model = Column(String(50))

    base_rate = Column(DECIMAL(10, 2))
    total_capacity = Column(Integer)
    available_capacity = Column(Integer)

    is_active = Column(Boolean, nullable=False, default=True)

    created_ts = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )
    updated_ts = Column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )
