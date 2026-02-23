from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas.vendor import VendorCreate, VendorUpdate, VendorResponse
from src.crud.vendor import (
    create_vendor,
    get_vendors,
    get_vendor,
    update_vendor,
    delete_vendor
)

router = APIRouter(prefix="/vendors", tags=["Vendors"])


@router.post("/", response_model=VendorResponse)
def create_vendor_endpoint(vendor: VendorCreate, db: Session = Depends(get_db)):
    return create_vendor(db, vendor)


@router.get("/", response_model=List[VendorResponse])
def list_vendors(db: Session = Depends(get_db)):
    return get_vendors(db)


@router.get("/{vendor_id}", response_model=VendorResponse)
def get_vendor_endpoint(vendor_id: int, db: Session = Depends(get_db)):
    return get_vendor(db, vendor_id)


@router.put("/{vendor_id}", response_model=VendorResponse)
def update_vendor_endpoint(vendor_id: int, vendor: VendorUpdate, db: Session = Depends(get_db)):
    return update_vendor(db, vendor_id, vendor)


@router.delete("/{vendor_id}")
def delete_vendor_endpoint(vendor_id: int, db: Session = Depends(get_db)):
    return delete_vendor(db, vendor_id)