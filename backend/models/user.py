from datetime import datetime
from pydantic import BaseModel
import enum
from fastapi import Query


class Role(enum.Enum):
    admin: str = "admin"
    personal: str = "personal"


class TypeID(enum.Enum):
    cni: str = "CNI"
    passport: str = "passport"


class User(BaseModel):
    first_name: str
    last_name: str
    birthdate: str
    id_type: TypeID
    contact: str
    login: str
    password: str
    mail: str = Query(..., regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+).([a-zA-Z]{2,5})$")
    role: Role

