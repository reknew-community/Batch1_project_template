from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.models.trip import TripDB
from src.schemas.trip import TripCreate, TripOut

router = APIRouter(prefix="/trips", tags=["Trips"])

@router.get("/", response_model=List[TripOut])
def list_trips(db: Session = Depends(get_db)):
    return db.query(TripDB).order_by(TripDB.id.desc()).all()

@router.get("/{trip_id}", response_model=TripOut)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    row = db.query(TripDB).filter(TripDB.id == trip_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Trip not found")
    return row

@router.post("/", response_model=TripOut)
def create_trip(payload: TripCreate, db: Session = Depends(get_db)):
    # enforce unique trip_code
    exists = db.query(TripDB).filter(TripDB.trip_code == payload.trip_code).first()
    if exists:
        raise HTTPException(status_code=409, detail="trip_code already exists")

    row = TripDB(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row