from jose import JWTError, jwt

from datetime import datetime, timedelta, timezone
from . import schemas

from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import database

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# SECRET_KEY
SECRET_KEY = "ajbndjasdjaujdadjasdjajdsdajwbdjsdjiawbdjansdjk"

# ALGORITHM
ALGORITHM = "HS256"

# expiration time
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(
token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)
):
credentials_exception = HTTPException(
status_code=status.HTTP_401_UNAUTHORIZED,
detail=f"Could not validate credentials",
headers={"WWW-Authenticate": "Bearer"},
)
return verify_token(token, credentials_exception)
