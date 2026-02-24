from fastapi import FastAPI
from src.database import engine, Base, settings

from src.routers.awbs import router as awbs_router
from src.routers.shipments import router as shipments_router

# IMPORTANT: import models so Base knows tables
from src.models import Hub, Route, RouteHub, Booking  # noqa: F401

from src.routers import hubs_router, routes_router, bookings_router
from src.routers.route_hubs import router as route_hubs_router  # ✅ add this

src = FastAPI(title="Logistics Data Platform")

# Create tables ONLY for local testing
if settings.AUTO_CREATE_TABLES:
    Base.metadata.create_all(bind=engine)

src.include_router(hubs_router)
src.include_router(routes_router)
src.include_router(bookings_router)
src.include_router(route_hubs_router)  
src.include_router(awbs_router) 
src.include_router(shipments_router)

@src.get("/")
def root():
    return {"message": "FastAPI is running"}