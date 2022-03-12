from pydantic import BaseModel


class JWTUser(BaseModel):
    username: str
    password: str
    role: str
    disabled: bool
