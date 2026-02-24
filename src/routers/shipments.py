from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from db_models import ShipmentDB, AwbDB
from models import Shipment, ShipmentCreate

from fastapi import APIRouter



router = APIRouter(prefix="/shipments", tags=["Shipments"])

@router.get("/", response_model=List[Shipment])
def list_shipments(db: Session = Depends(get_db)):
    return db.query(ShipmentDB).order_by(ShipmentDB.id.desc()).all()

@router.post("/", response_model=Shipment)
def create_shipment(payload: ShipmentCreate, db: Session = Depends(get_db)):
    row = ShipmentDB(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row