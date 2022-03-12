from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from utils.security import check_jwt_token
from starlette.status import HTTP_401_UNAUTHORIZED
from routes.v1 import app_v1

app = FastAPI()
app.mount("/v1", app_v1)


@app.middleware("http")
async def middleware(request: Request, call_next):
    if not str(request.url).__contains__("/token"):
        try:
            jwt_token = (request.headers["Authorization"]).split(" ")[1]
            is_valid = check_jwt_token(jwt_token)
        except Exception as e:
            is_valid = False
        if not is_valid:
            return Response("Unauthorized", status_code=HTTP_401_UNAUTHORIZED)
    response = await call_next(request)
    return response
