from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.model.user import User
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_lower_string


def create_random_user(db: Session) -> UserCreate:
    username = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(username=username, password=password)
    crud.user.create(db=db, obj_in=user_in)
    return user_in