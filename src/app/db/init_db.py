from sqlalchemy.orm import Session

import csv
import os.path
from app.db.session import SessionLocal
from sqlalchemy.orm import Session


from app import crud, schemas


def init_db(db: Session) -> None:

    db = SessionLocal()

    my_path = os.path.abspath(os.path.dirname(__file__))
    with open (os.path.join(my_path, "../../data/users.csv"), newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print("#######criando")
            createUser(db,row['username'], row['password'])
    
    with open (os.path.join(my_path, "../../data/vehicles.csv"), newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            createVehicle(db,row['id'], row['distance'], row['owner'])

    

def createUser(db: Session, username: str, password: str):
    user = crud.user.get_by_username(db, username=username)
    if not user:
        user_in = schemas.UserCreate(
            username=username,
            password=password,
        )
        crud.user.create(db, obj_in=user_in)

def createVehicle(db: Session, id: int, distance: int, owner: str):
    vehicle = crud.vehicle.get(db, id=id)
    if not vehicle:
        vehicle_in = schemas.VehicleCreate(
            id=id,
            distance=distance,
            owner=owner,
        )
        crud.vehicle.create(db, obj_in=vehicle_in)
