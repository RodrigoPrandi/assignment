from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    username: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
