from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db

from src.models.awb import AwbDB


from src.schemas.awb import Awb, AwbCreate

router = APIRouter(prefix="/awbs", tags=["AWB"])


@router.get("/", response_model=List[Awb], summary="List AWBs")
def list_awbs(db: Session = Depends(get_db)):
    return db.query(AwbDB).order_by(AwbDB.id.desc()).all()


@router.post("/", response_model=Awb, summary="Create AWB")
def create_awb(payload: AwbCreate, db: Session = Depends(get_db)):
    # awb_number is UNIQUE in your DB
    exists = db.query(AwbDB).filter(AwbDB.awb_number == payload.awb_number).first()
    if exists:
        raise HTTPException(status_code=400, detail="awb_number already exists")

    row = AwbDB(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("/{id}", response_model=Awb, summary="Get AWB by id")
def get_awb(id: int, db: Session = Depends(get_db)):
    row = db.query(AwbDB).filter(AwbDB.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="AWB not found")
    return row


@router.put("/{id}", response_model=Awb, summary="Update AWB by id")
def update_awb(id: int, payload: AwbCreate, db: Session = Depends(get_db)):
    row = db.query(AwbDB).filter(AwbDB.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="AWB not found")

    # Update fields
    row.awb_number = payload.awb_number
    row.customer_id = payload.customer_id
    row.booking_id = payload.booking_id
    row.status = payload.status
    row.generated_ts = payload.generated_ts
    row.assigned_ts = payload.assigned_ts
    row.used_at = payload.used_at

    db.commit()
    db.refresh(row)
    return row


@router.delete("/{id}", summary="Delete AWB by id")
def delete_awb(id: int, db: Session = Depends(get_db)):
    row = db.query(AwbDB).filter(AwbDB.id == id).first()
    if not row:
        raise HTTPException(status_code=404, detail="AWB not found")

    db.delete(row)
    db.commit()
    return {"message": "AWB deleted"}