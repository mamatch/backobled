from fastapi import FastAPI, Body, Header, File, Depends
from starlette.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from models.user import User
from utils.security import authenticate_user, create_jwt_token, check_jwt_token
from models.jwt_user import JWTUser

app_v1 = FastAPI(openapi_prefix="/v1")


# End points for users
@app_v1.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    jwt_user_dict = {"username": form_data.username, "password": form_data.password, "role": "admin", "disabled": False}
    jwt_user = JWTUser(**jwt_user_dict)
    user = authenticate_user(jwt_user)

    if user is None:
        return HTTPException(HTTP_401_UNAUTHORIZED)
    jwt_token = create_jwt_token(user)
    return {"token": jwt_token}


@app_v1.post("/user")
async def post_user(user: User, jwt: bool = Depends(check_jwt_token)):
    """
    A function to create a new user
    :param jwt:
    :param user: The user object containing the information
    :return:
    """
    return {"request body": user}


@app_v1.get("/user")
async def get_user_validation(password: str, jwt: bool = Depends(check_jwt_token)):
    """
    A function to know if a user exists
    :param jwt:
    :param password: The password of the user
    :return:
    """
    return {"parameter": password}


@app_v1.get("/users")
async def get_users(jwt: bool = Depends(check_jwt_token)):
    """
    A function to get all users
    :return:
    """
    return {"all_users": "all"}


@app_v1.put("/user/{id}")
async def modify_user(id: int, user: User, jwt: bool = Depends(check_jwt_token)):
    """
    A function to modify information about a user
    :param jwt:
    :param id: The id of the user
    :param user: The object
    :return:
    """
    return {"id": id, "update": user}


# Flight routes

@app_v1.get("/flights")
async def get_flights(jwt: bool = Depends(check_jwt_token)):
    return {"flightd": "all flights"}
