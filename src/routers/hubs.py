from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.hubs import Hub
from src.schemas.hubs import HubCreate, HubUpdate, HubOut

router = APIRouter(prefix="/hubs", tags=["Hubs"])

@router.get("/", response_model=list[HubOut])
def list_hubs(db: Session = Depends(get_db)):
    return db.query(Hub).all()

@router.post("/", response_model=HubOut)
def create_hub(payload: HubCreate, db: Session = Depends(get_db)):
    hub = Hub(**payload.model_dump())
    db.add(hub)
    db.commit()
    db.refresh(hub)
    return hub

@router.put("/{hub_id}", response_model=HubOut)
def update_hub(hub_id: int, payload: HubUpdate, db: Session = Depends(get_db)):
    hub = db.get(Hub, hub_id)
    if not hub:
        raise HTTPException(status_code=404, detail="Hub not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(hub, k, v)
    db.commit()
    db.refresh(hub)
    return hub

@router.delete("/{hub_id}")
def delete_hub(hub_id: int, db: Session = Depends(get_db)):
    hub = db.get(Hub, hub_id)
    if not hub:
        raise HTTPException(status_code=404, detail="Hub not found")
    db.delete(hub)
    db.commit()
    return {"message": "deleted"}