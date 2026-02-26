from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.models.vendor_performance import VendorPerformanceDB
from src.schemas.vendor_performance import VendorPerformanceCreate, VendorPerformanceOut

router = APIRouter(prefix="/vendor-performance", tags=["Vendor Performance"])

@router.get("/", response_model=List[VendorPerformanceOut])
def list_vendor_performance(db: Session = Depends(get_db)):
    return db.query(VendorPerformanceDB).order_by(VendorPerformanceDB.id.desc()).all()

@router.get("/{vp_id}", response_model=VendorPerformanceOut)
def get_vendor_performance(vp_id: int, db: Session = Depends(get_db)):
    row = db.query(VendorPerformanceDB).filter(VendorPerformanceDB.id == vp_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Vendor performance record not found")
    return row

@router.post("/", response_model=VendorPerformanceOut)
def create_vendor_performance(payload: VendorPerformanceCreate, db: Session = Depends(get_db)):
    row = VendorPerformanceDB(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row