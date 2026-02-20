from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models.customer import Customer

from app.database import get_db
from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)
from app.crud.customer import (
    create_customer,
    get_customers,
    get_customer_by_id,
    update_customer,
    deactivate_customer
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

# -----------------------------
# GET – Fetch all customers
# -----------------------------
@router.get("/", response_model=List[CustomerResponse])
def read_customers(db: Session = Depends(get_db)):
    return get_customers(db)


# -----------------------------
# POST – Create customer
# -----------------------------
@router.post(
    "/",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED
)
def create(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)


# -----------------------------
# GET – Fetch one customer
# -----------------------------
@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


# -----------------------------
# PUT – Update customer
# -----------------------------
@router.put("/{customer_id}", response_model=CustomerResponse)
def update(
    customer_id: int,
    customer_update: CustomerUpdate,
    db: Session = Depends(get_db)
):
    customer = get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return update_customer(db, customer, customer_update)



@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    db.delete(customer)
    db.commit()

    return {"message": "Customer deleted successfully"}
