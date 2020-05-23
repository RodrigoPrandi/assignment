from fastapi import APIRouter, Depends
from app.model.vehicle import Vehicle
from app.model.user import User
from app.api.utils.security import get_current_active_user

router = APIRouter()

@router.get("/", response_model=Vehicle)
def vehicles(current_user: User = Depends(get_current_active_user)):
    ob = Vehicle()
    ob.id = 1
    ob.distance = 132
    ob.owner = "current_user.username"
    return ob