from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.routes import Route
from src.schemas.routes import RouteCreate, RouteUpdate, RouteOut

router = APIRouter(prefix="/routes", tags=["Routes"])


@router.get("/", response_model=list[RouteOut])
def list_routes(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
    origin_city: str | None = None,
    destination_city: str | None = None,
    is_active: bool | None = None,
    db: Session = Depends(get_db),
):
    q = db.query(Route)

    if origin_city:
        q = q.filter(Route.origin_city == origin_city)
    if destination_city:
        q = q.filter(Route.destination_city == destination_city)
    if is_active is not None:
        q = q.filter(Route.is_active == is_active)

    return q.offset((page - 1) * page_size).limit(page_size).all()


@router.get("/{route_id}", response_model=RouteOut)
def get_route(route_id: int, db: Session = Depends(get_db)):
    route = db.get(Route, route_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")
    return route


@router.post("/", response_model=RouteOut)
def create_route(payload: RouteCreate, db: Session = Depends(get_db)):
    route = Route(**payload.model_dump())
    db.add(route)
    db.commit()
    db.refresh(route)
    return route


@router.put("/{route_id}", response_model=RouteOut)
def update_route(route_id: int, payload: RouteUpdate, db: Session = Depends(get_db)):
    route = db.get(Route, route_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")

    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(route, k, v)

    db.commit()
    db.refresh(route)
    return route


@router.delete("/{route_id}")
def delete_route(route_id: int, db: Session = Depends(get_db)):
    route = db.get(Route, route_id)
    if not route:
        raise HTTPException(status_code=404, detail="Route not found")

    db.delete(route)
    db.commit()
    return {"message": "deleted"}