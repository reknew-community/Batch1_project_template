from sqlalchemy import Column, BigInteger, String
from src.database import Base

class AwbDB(Base):
    __tablename__ = "awbs"  # must match your DB table name

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    awb_number = Column(String(50), unique=True, nullable=False)
    customer_id = Column(BigInteger, nullable=False)
    booking_id = Column(BigInteger, nullable=False)
    status = Column(String(30), nullable=False)
    generated_ts = Column(String(50), nullable=False)
    assigned_ts = Column(String(50), nullable=True)
    used_at = Column(String(50), nullable=True)