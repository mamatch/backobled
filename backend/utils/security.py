import time

from passlib.context import CryptContext
from datetime import datetime, timedelta
from utils.const import JWT_EXPIRATION_TIME_MINUTES, JWT_SECRET_KEY, JWT_ALGORITHM
from models.jwt_user import JWTUser
import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.exceptions import HTTPException

oauth_scheme = OAuth2PasswordBearer("/token")  # Oauth schema
pwd_context = CryptContext(schemes="bcrypt")  # password context
jwt_user = {"username": "dej", "password": "$2b$12$cM2K2vkwPcvysryi5x5l2.gAMIQ0gVo0p73D0rZrD8MU6zl7dIpLC",
            "disabled": False, "role": "admin"}
mock_jwt_user = JWTUser(**jwt_user)


def get_hashed_password(password: str):
    """
    A function to hash the password
    :param password: The password to hash
    :return: The hashed password
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    """
    A function to verify if a password corresponds to a hashed value
    :param plain_password: The password to hash
    :param hashed_password: The hashed password
    :return:
    """
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        return False


def authenticate_user(user: JWTUser):
    if mock_jwt_user.username == user.username:
        if verify_password(user.password, mock_jwt_user.password):
            user.role = "admin"
            return user

    raise HTTPException(HTTP_401_UNAUTHORIZED)


def create_jwt_token(user: JWTUser):
    """
    A function to create a jwt token
    :param user:
    :return:
    """
    expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    jwt_payload = {"sub": user.username,"role": user.role, "exp": expiration}

    token = jwt.encode(jwt_payload, key=JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token


def check_jwt_token(token: str = Depends(oauth_scheme)):
    try:
        jwt_payload = jwt.decode(token, key=JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")
        if time.time() < expiration:
            if username == mock_jwt_user.username:
                return final_checks(role)
    except Exception as e:
        raise HTTPException(HTTP_401_UNAUTHORIZED)


def final_checks(role: str):
    if role == "admin":
        return True
    else:
        raise HTTPException(HTTP_401_UNAUTHORIZED)
