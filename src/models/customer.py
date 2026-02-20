from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    customer_code = Column(String(50), unique=True, nullable=False)
    name = Column(String(150), nullable=False)

    contact_person = Column(String(150))
    email = Column(String(150))
    phone = Column(String(20))

    address = Column(Text)
    city = Column(String(100))
    state = Column(String(100))
    pincode = Column(String(20))
    country = Column(String(100))

    credit_rating = Column(String(20))
    is_active = Column(Boolean, default=True, nullable=False)

    created_ts = Column(DateTime(timezone=True), server_default=func.now())
    updated_ts = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
