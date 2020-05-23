import jwt

from app.core.config import settings
from datetime import datetime, timedelta

access_token_jwt_subject = "access"


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=10)
    to_encode.update({"exp": expire, "sub": access_token_jwt_subject})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
