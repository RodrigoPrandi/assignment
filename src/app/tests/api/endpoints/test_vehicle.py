from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.utils import get_token_headers, random_lower_string
from app.tests.utils.user import create_random_user, drop_user
from app.tests.utils.vehicle import create_vehicle


def test_without_authentication_token(
    client: TestClient, db: Session
) -> None:
    response = client.get(
        "/vehicles",
    )
    assert response.status_code == 401
    content = response.json()
    assert "detail" in content
    assert "Not authenticated" == content["detail"]


def test_with_authentication_invalid(
    client: TestClient, db: Session
) -> None:
    response = client.get(
        "/vehicles", headers={"Authorization": "Bearer InvalidToken"},
    )
    assert response.status_code == 403
    content = response.json()
    assert "detail" in content
    assert "Could not validate credentials" == content["detail"]

def test_with_user_not_found(
    client: TestClient, db: Session
) -> None:
    password = random_lower_string()
    user = create_random_user(db, password=password)

    headers = get_token_headers(client, user.username, password)

    drop_user(db,user.id)

    response = client.get(
        "/vehicles", headers=headers,
    )
    assert response.status_code == 404
    content = response.json()
    assert "detail" in content
    assert "User not found" == content["detail"]


def test_empty_user_vehicles(
    client: TestClient, db: Session
) -> None:
    password = random_lower_string()
    user = create_random_user(db, password=password)

    headers = get_token_headers(client, user.username, password)

    response = client.get(
        "/vehicles", headers=headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert [] == content

def test_user_vehicles(
    client: TestClient, db: Session
) -> None:
    password = random_lower_string()
    user = create_random_user(db, password=password)

    veicle300 = create_vehicle(db, user.username, 300)
    veicle10 = create_vehicle(db, user.username, 10)

    headers = get_token_headers(client, user.username, password)

    response = client.get(
        "/vehicles", headers=headers,
    )
    

    expected_Json = [{
        "distance": veicle10.distance,
        "owner": veicle10.owner,
        "id": veicle10.id
    },
    {
        "distance": veicle300.distance,
        "owner": veicle300.owner,
        "id": veicle300.id
    }
    ]


    assert response.status_code == 200
    content = response.json()
    assert expected_Json == content