from sqlalchemy.orm import Session
from src.models.customer import Customer
from src.schemas.customer import CustomerCreate, CustomerUpdate


# -------------------------
# Create Customer
# -------------------------
def create_customer(db: Session, customer: CustomerCreate) -> Customer:
    # Generate a new ID manually since 'id' is not AUTO_INCREMENT
    last_customer = db.query(Customer).order_by(Customer.id.desc()).first()
    new_id = 1 if not last_customer else last_customer.id + 1

    db_customer = Customer(
        id=new_id,  # manually set ID
        customer_code=customer.customer_code,
        name=customer.name,
        contact_person=customer.contact_person,
        email=customer.email,
        phone=customer.phone,
        address=customer.address,
        city=customer.city,
        state=customer.state,
        pincode=customer.pincode,
        country=customer.country,
        credit_rating=customer.credit_rating,
        is_active=customer.is_active,
    )

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


# -------------------------
# Get Customer by ID
# -------------------------
def get_customer_by_id(db: Session, customer_id: int) -> Customer | None:
    return db.query(Customer).filter(Customer.id == customer_id).first()


# -------------------------
# Get All Customers
# -------------------------
def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()


# -------------------------
# Update Customer
# -------------------------
def update_customer(
    db: Session,
    db_customer: Customer,
    customer_update: CustomerUpdate
) -> Customer:

    update_data = customer_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_customer, field, value)

    db.commit()
    db.refresh(db_customer)
    return db_customer


# -------------------------
# Soft Delete (Deactivate)
# -------------------------
def deactivate_customer(db: Session, db_customer: Customer) -> Customer:
    db_customer.is_active = False
    db.commit()
    db.refresh(db_customer)
    return db_customer