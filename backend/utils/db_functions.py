from models.jwt_user import JWTUser
from utils.db import execute, fetch


async def db_check_jwt_user(user: JWTUser):
    query = """
    select * 
    from users 
    where username = :username 
    and password = :password 
    """
    values = {"username": user.username, "password": user.password}

    result = await fetch(query=query, is_one=True, values=values)
    if result is None:
        return False
    else:
        return True


async def db_check_username(username: str):
    query = """
    select *
    from users
    where username = :username
    """
    values = {"username": username}
    result = await fetch(query, True, values)
    if result is not None:
        return True
    return False
