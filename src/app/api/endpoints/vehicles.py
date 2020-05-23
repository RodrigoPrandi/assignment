from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app import crud, model, schemas
from app.api.utils import security

router = APIRouter()

@router.get("/", response_model=List[schemas.Vehicle])
def get_all_vehicles(db: Session = Depends(security.get_db), current_user: model.User = Depends(security.get_current_user)):
    
    vehicles = crud.vehicle.get_multi_by_owner(
        db=db, owner_id=current_user.username
    )
    return vehicles