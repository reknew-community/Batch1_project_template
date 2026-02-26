from fastapi import FastAPI
from src.database import engine, Base, settings

# Import existing models
from src.models import Hub, Route, Booking  
from src.models import roles, user, customer, vendor  

# Import existing routers
from src.routers import hubs_router, routes_router, bookings_router
from src.routers import user, vendor, roles, customer
from src.routers.awbs import router as awbs_router
from src.routers.shipments import router as shipments_router
from src.routers.trip import router as trips_router
from src.routers.vendor_performance import router as vendor_performance_router


# Initialize FastAPI app
app = FastAPI(title="Logistics & Management API")

# Create tables only if AUTO_CREATE_TABLES = True
if settings.AUTO_CREATE_TABLES:
    Base.metadata.create_all(bind=engine)

# Existing logistics routers
app.include_router(hubs_router)
app.include_router(routes_router)
app.include_router(bookings_router)
app.include_router(roles.router)
app.include_router(user.router)
app.include_router(customer.router)
app.include_router(vendor.router)
app.include_router(awbs_router) 
app.include_router(shipments_router)
app.include_router(trips_router)
app.include_router(vendor_performance_router)


# Root endpoint
@app.get("/")
def root():
    return {"message": "FastAPI is running"}