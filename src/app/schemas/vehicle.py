from typing import Optional

from pydantic import BaseModel


# Shared properties
class VehicleBase(BaseModel):
    distance: int = None
    owner: str = None


# Properties to receive on vehicle creation
class VehicleCreate(VehicleBase):
    pass


# Properties shared by model stored in DB
class VehicleInDBBase(VehicleBase):
    id: int
    distance: int
    owner: str

    class Config:
        orm_mode = True


# Properties to return to client
class Vehicle(VehicleInDBBase):
    pass


# Properties properties stored in DB
class VehicleInDB(VehicleInDBBase):
    pass
