from typing import Dict
import random

from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from app.tests.utils.utils import random_lower_string
from app.tests.utils.user import create_random_user


def test_get_access_token_with_invalid_user(client: TestClient) -> None:
    login_data = {
        "username": random_lower_string(),
        "password": random_lower_string(),
    }
    r = client.post("/token", data=login_data)
    tokens = r.json()
    assert r.status_code == 401
    assert "detail" in tokens
    assert "Incorrect username or password" == tokens["detail"]

def test_get_access_token_with_invalid_password(client: TestClient, db: Session) -> None:
    user = create_random_user(db)
    
    login_data = {
        "username": user.username,
        "password": random_lower_string(),
    }
    r = client.post("/token", data=login_data)
    tokens = r.json()
    assert r.status_code == 401
    assert "detail" in tokens
    assert "Incorrect username or password" == tokens["detail"]


def test_get_access_token(client: TestClient, db: Session) -> None:
    user = create_random_user(db)
    
    login_data = {
        "username": user.username,
        "password": user.password,
    }
    r = client.post("/token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]