from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True)
    phone = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))

    user_id = Column(Integer, ForeignKey("users.id"))  # link to users
    user = relationship("User", back_populates="customers")