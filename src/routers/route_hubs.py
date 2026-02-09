from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.route_hubs import RouteHub  # if your file name is routehubs.py
from src.models.routes import Route
from src.models.hubs import Hub
from src.schemas.route_hubs import RouteHubCreate, RouteHubUpdate, RouteHubOut

router = APIRouter(tags=["Route Hubs"])


@router.get("/routes/{route_id}/hubs", response_model=list[RouteHubOut])
def list_hubs_for_route(route_id: int, db: Session = Depends(get_db)):
    # Ensure route exists
    route = db.get(Route, route_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")

    return (
        db.query(RouteHub)
        .filter(RouteHub.route_id == route_id)
        .order_by(RouteHub.sequence_no)
        .all()
    )


@router.post("/routes/{route_id}/hubs", response_model=RouteHubOut)
def add_hub_to_route(route_id: int, payload: RouteHubCreate, db: Session = Depends(get_db)):
    # Ensure route exists
    route = db.get(Route, route_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")

    # Ensure hub exists
    hub = db.get(Hub, payload.hub_id)
    if not hub:
        raise HTTPException(status_code=404, detail="Hub not found")

    # Create msrcing (route_id comes from path, hub_id & sequence_no from body)
    link = RouteHub(route_id=route_id, hub_id=payload.hub_id, sequence_no=payload.sequence_no)

    db.add(link)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        # This typically hsrcens due to unique constraints (duplicate sequence_no or duplicate hub on route)
        raise HTTPException(status_code=400, detail=f"Could not add hub to route: {str(e)}")

    db.refresh(link)
    return link


@router.put("/route-hubs/{route_hub_id}", response_model=RouteHubOut)
def update_route_hub(route_hub_id: int, payload: RouteHubUpdate, db: Session = Depends(get_db)):
    link = db.get(RouteHub, route_hub_id)
    if not link:
        raise HTTPException(status_code=404, detail="RouteHub msrcing not found")

    link.sequence_no = payload.sequence_no

    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Could not update route hub: {str(e)}")

    db.refresh(link)
    return link


@router.delete("/route-hubs/{route_hub_id}")
def delete_route_hub(route_hub_id: int, db: Session = Depends(get_db)):
    link = db.get(RouteHub, route_hub_id)
    if not link:
        raise HTTPException(status_code=404, detail="RouteHub msrcing not found")

    db.delete(link)
    db.commit()
    return {"message": "deleted"}