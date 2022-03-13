from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.requests import Request
from starlette.responses import Response

from models.jwt_user import JWTUser
from utils.security import check_jwt_token, authenticate_user, create_jwt_token
from starlette.status import HTTP_401_UNAUTHORIZED
from routes.v1 import app_v1

from fastapi.exceptions import HTTPException

app = FastAPI(title="BackoBled API Document", description="Test description", version="1.0.0")
app.include_router(app_v1, prefix="/v1", dependencies=[Depends(check_jwt_token)])


@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    A function to authenticate a user
    :param form_data: The form used to authenticate
    :return:
    """
    jwt_user_dict = {"username": form_data.username, "password": form_data.password, "role": "admin", "disabled": False}
    jwt_user = JWTUser(**jwt_user_dict)
    user = await authenticate_user(jwt_user)

    if user is None:
        return HTTPException(HTTP_401_UNAUTHORIZED)
    jwt_token = await create_jwt_token(user)
    return {"access_token": jwt_token}


@app.middleware("http")
async def middleware(request: Request, call_next):
    if not any([word in str(request.url) for word in ["/token", "/docs", "/openapi.json"]]):
        try:
            jwt_token = (request.headers["Authorization"]).split(" ")[1]
            is_valid = await check_jwt_token(jwt_token)
        except Exception as e:
            is_valid = False
        if not is_valid:
            return Response("Unauthorized", status_code=HTTP_401_UNAUTHORIZED)
    response = await call_next(request)
    return response
