from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.vendor import VendorCreate, VendorUpdate, VendorResponse
from app.crud.vendor import (
    get_vendors,
    get_vendor_by_id,
    create_vendor,
    update_vendor,
    deactivate_vendor
)

router = APIRouter(
    prefix="/vendors",
    tags=["Vendors"]
)

# -----------------------------
# GET – All vendors
# -----------------------------
@router.get("/", response_model=List[VendorResponse])
def read_vendors(db: Session = Depends(get_db)):
    return get_vendors(db)


# -----------------------------
# POST – Create vendor
# -----------------------------
@router.post("/", response_model=VendorResponse, status_code=status.HTTP_201_CREATED)
def create(vendor: VendorCreate, db: Session = Depends(get_db)):
    return create_vendor(db, vendor)


# -----------------------------
# PUT – Update vendor
# -----------------------------
@router.put("/{vendor_id}", response_model=VendorResponse)
def update(
    vendor_id: int,
    vendor_update: VendorUpdate,
    db: Session = Depends(get_db)
):
    db_vendor = get_vendor_by_id(db, vendor_id)
    if not db_vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    return update_vendor(db, db_vendor, vendor_update)


# -----------------------------
# DELETE – Soft delete vendor
# -----------------------------
@router.delete("/{vendor_id}")
def delete(vendor_id: int, db: Session = Depends(get_db)):
    db_vendor = get_vendor_by_id(db, vendor_id)
    if not db_vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    deactivate_vendor(db, db_vendor)
    return {"message": "Vendor deactivated successfully"}
