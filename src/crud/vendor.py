from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.vendor import Vendor
from src.schemas.vendor import VendorCreate, VendorUpdate


# ----------- CREATE -----------
def create_vendor(db: Session, vendor: VendorCreate):
    db_vendor = Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor


# ----------- GET ALL -----------
def get_vendors(db: Session):
    return db.query(Vendor).all()


# ----------- GET BY ID -----------
def get_vendor(db: Session, vendor_id: int):
    vendor = db.query(Vendor).filter(Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor


# ----------- UPDATE -----------
def update_vendor(db: Session, vendor_id: int, vendor_update: VendorUpdate):
    vendor = db.query(Vendor).filter(Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    for key, value in vendor_update.dict(exclude_unset=True).items():
        setattr(vendor, key, value)

    db.commit()
    db.refresh(vendor)
    return vendor


# ----------- DELETE -----------
def delete_vendor(db: Session, vendor_id: int):
    vendor = db.query(Vendor).filter(Vendor.id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    db.delete(vendor)
    db.commit()
    return {"message": "Vendor deleted successfully"}