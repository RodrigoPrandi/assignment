from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.model.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate


class CRUDVehicle(CRUDBase[Vehicle, VehicleCreate]):
    def get_all_by_owner_order_by_distance(
        self, db: Session, *, owner: str
    ) -> List[Vehicle]:
        return (
            db.query(self.model)
            .filter(Vehicle.owner == owner)
            .order_by(Vehicle.distance.asc())
            .all()
        )


vehicle = CRUDVehicle(Vehicle)
