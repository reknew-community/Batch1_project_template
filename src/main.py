from fastapi import FastAPI
from src.database import engine, Base, settings

# Import existing logistics models
from src.models import Hub, Route, RouteHub, Booking  

# Import new management models
from src.models import roles, user, customer, vendor  

# Import existing routers
from src.routers import hubs_router, routes_router, bookings_router
from src.routers.route_hubs import router as route_hubs_router

# Import new routers
from src.routers import user, vendor, roles, customer

from src.routers.awbs import router as awbs_router
from src.routers.shipments import router as shipments_router


# Initialize FastAPI app
app = FastAPI(title="Logistics & Management API")

# Create tables only if AUTO_CREATE_TABLES = True
if settings.AUTO_CREATE_TABLES:
    Base.metadata.create_all(bind=engine)

# Existing logistics routers
app.include_router(hubs_router)
app.include_router(routes_router)
app.include_router(bookings_router)
app.include_router(route_hubs_router)

# New management routers
app.include_router(roles.router)
app.include_router(user.router)
app.include_router(customer.router)
app.include_router(vendor.router)
app.include_router(awbs_router) 
app.include_router(shipments_router)


# Root endpoint
@app.get("/")
def root():
    return {"message": "FastAPI is running"}