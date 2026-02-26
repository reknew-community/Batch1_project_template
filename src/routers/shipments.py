from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.models.shipment import ShipmentDB  # SQLAlchemy model
from src.schemas.shipment import ShipmentCreate, Shipment  # Pydantic schemas

router = APIRouter(prefix="/shipments", tags=["ShipmentDB"])


@router.get("/", response_model=List[Shipment])
def list_shipments(db: Session = Depends(get_db)):
    return db.query(Shipment).order_by(Shipment.id.desc()).all()


@router.post("/", response_model=Shipment)
def create_shipment(payload: ShipmentCreate, db: Session = Depends(get_db)):
    row = Shipment(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row