from sqlalchemy import Column, BigInteger, String, Boolean, Text
from src.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True, index=True)
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
    is_active = Column(Boolean, default=True)

    created_ts = Column(String(50), nullable=False)
    updated_ts = Column(String(50), nullable=False)
    
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from src.database import Base

# class Customer(Base):
#     __tablename__ = "customers"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(255), nullable=False)
#     email = Column(String(255), unique=True)
#     phone = Column(String(50))
#     city = Column(String(50))
#     state = Column(String(50))

#     user_id = Column(Integer, ForeignKey("users.id"))  # link to users
#     user = relationship("User", back_populates="customers")