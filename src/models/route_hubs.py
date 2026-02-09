from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from src.database import Base

class RouteHub(Base):
    __tablename__ = "route_hubs"
    __table_args__ = (
        UniqueConstraint("route_id", "sequence_no", name="uq_route_sequence"),
        UniqueConstraint("route_id", "hub_id", name="uq_route_hub"),
    )

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"), nullable=False)
    hub_id = Column(Integer, ForeignKey("hubs.id"), nullable=False)
    sequence_no = Column(Integer, nullable=False)