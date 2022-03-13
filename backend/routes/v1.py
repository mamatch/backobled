from fastapi import FastAPI, Body, Header, File, Depends, APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from models.user import User
from utils.security import authenticate_user, create_jwt_token
from models.jwt_user import JWTUser

app_v1 = APIRouter()


# End points for users


@app_v1.post("/user", description="Create a new user", summary="Create a new user")
async def post_user(user: User):
    """
    A function to create a new user
    :param user: The user object containing the information
    :return:
    """
    return {"request body": user}


@app_v1.get("/users", summary="Get all the users")
async def get_users():
    """
    A function to get all users
    :return:
    """
    return {"all_users": "all"}


@app_v1.put("/user/{id}")
async def modify_user(id: int, user: User):
    """
    A function to modify information about a user
    :param id: The id of the user
    :param user: The object
    :return:
    """
    return {"id": id, "update": user}


# Flight routes

@app_v1.get("/flights")
async def get_flights():
    return {"flightd": "all flights"}
