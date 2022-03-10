from datetime import datetime

from pydantic import BaseModel
import enum
from fastapi import Query


class Country(BaseModel):
    name: str