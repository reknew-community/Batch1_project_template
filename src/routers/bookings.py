from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.bookings import Booking
from src.schemas.bookings import BookingCreate, BookingUpdate, BookingOut

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("/", response_model=list[BookingOut])
def list_bookings(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
    customer_id: int | None = None,
    status: str | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(Booking)

    if customer_id is not None:
        q = q.filter(Booking.customer_id == customer_id)
    if status:
        q = q.filter(Booking.status == status)

    return q.offset((page - 1) * page_size).limit(page_size).all()


@router.get("/{booking_id}", response_model=BookingOut)
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.get(Booking, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


@router.post("/", response_model=BookingOut)
def create_booking(payload: BookingCreate, db: Session = Depends(get_db)):
    booking = Booking(**payload.model_dump())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


@router.put("/{booking_id}", response_model=BookingOut)
def update_booking(booking_id: int, payload: BookingUpdate, db: Session = Depends(get_db)):
    booking = db.get(Booking, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(booking, k, v)

    db.commit()
    db.refresh(booking)
    return booking


@router.delete("/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.get(Booking, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    db.delete(booking)
    db.commit()
    return {"message": "deleted"}