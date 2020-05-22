from pydantic import BaseModel

class Vehicle(BaseModel):
    id: int = None
    distance: int = None
    owner:str = None