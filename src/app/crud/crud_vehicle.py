from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.model.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate


class CRUDVehicle(CRUDBase[Vehicle, VehicleCreate]):
    def create_with_owner(
        self, db: Session, *, obj_in: VehicleCreate, owner_id: int
    ) -> Vehicle:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner: str
    ) -> List[Vehicle]:
        return (
            db.query(self.model)
            .filter(Vehicle.owner == owner)
            .all()
        )


vehicle = CRUDVehicle(Vehicle)
