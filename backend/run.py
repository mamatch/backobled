from fastapi import FastAPI

from models.user import User

app = FastAPI()


# End points for users
@app.post("/user")
async def post_user(user: User):
    """
    A function to create a new user
    :param user: The user object containing the information
    :return:
    """
    return {"request body": user}


@app.get("/user")
async def get_user_validation(password: str):
    """
    A function to know if a user exists
    :param password: The password of the user
    :return:
    """
    return {"parameter": password}


@app.put("/user")
async def modify_user(id: int, user: User):
    """
    A function to modify information about a user
    :param id: The id of the user
    :param user: The object
    :return:
    """
    pass


@app.get("/hello")
async def hello_world():
    return {"Hello world!!!"}
