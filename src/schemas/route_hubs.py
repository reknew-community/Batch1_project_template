from pydantic import BaseModel, Field

class RouteHubCreate(BaseModel):
    hub_id: int
    sequence_no: int = Field(ge=1)

class RouteHubUpdate(BaseModel):
    sequence_no: int = Field(ge=1)

class RouteHubOut(BaseModel):
    id: int
    route_id: int
    hub_id: int
    sequence_no: int

    class Config:
        from_attributes = True