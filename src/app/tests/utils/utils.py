import random
import string
from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def get_token_headers(client: TestClient, username: str, password: str) -> Dict[str, str]:
    login_data = {
        "username": username,
        "password": password,
    }
    r = client.post("/token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers