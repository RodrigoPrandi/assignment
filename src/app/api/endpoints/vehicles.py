from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app import crud, model, schemas
from app.api.utils import security

router = APIRouter()

@router.get("/", response_model=List[schemas.Vehicle])
def get_all_vehicles(db: Session = Depends(security.get_db), current_user: model.User = Depends(security.get_current_user)):
    
    vehicles = crud.vehicle.get_all_by_owner_order_by_distance(
        db=db, owner=current_user.username
    )
    return vehicles