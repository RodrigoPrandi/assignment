from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.model.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate
from app.tests.utils.utils import random_lower_string


def create_vehicle(db: Session, owner: str, distance: int) -> Vehicle:
    vehicle_in = VehicleCreate(owner=owner, distance = distance)
    return crud.vehicle.create(db=db, obj_in=vehicle_in)


def drop_user(db: Session, id: int):
    crud.user.remove(db=db, id=id)