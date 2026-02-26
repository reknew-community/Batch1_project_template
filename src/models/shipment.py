from sqlalchemy import Column, BigInteger, String, DECIMAL
from src.database import Base

class ShipmentDB(Base):
    __tablename__ = "shipments"  # must match your DB table name

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    awb_id = Column(BigInteger, nullable=False)
    customer_id = Column(BigInteger, nullable=False)
    booking_id = Column(BigInteger, nullable=False)

    origin_city = Column(String(100), nullable=True)
    destination_city = Column(String(100), nullable=True)

    weight_kg = Column(DECIMAL(10, 2), nullable=True)
    current_status = Column(String(50), nullable=True)