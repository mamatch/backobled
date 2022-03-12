from fastapi import FastAPI
from models.user import User

app_v1 = FastAPI(openapi_prefix="/v1")


# End points for users
@app_v1.post("/user")
async def post_user(user: User):
    """
    A function to create a new user
    :param user: The user object containing the information
    :return:
    """
    return {"request body": user}


@app_v1.get("/user")
async def get_user_validation(password: str):
    """
    A function to know if a user exists
    :param password: The password of the user
    :return:
    """
    return {"parameter": password}


@app_v1.get("/users")
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
