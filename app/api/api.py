from fastapi import APIRouter

from app.api.endpoints import token, vehicles

api_router = APIRouter()
api_router.include_router(token.router, tags=["token"])
api_router.include_router(vehicles.router, prefix="/vehicles", tags=["vehicles"])
