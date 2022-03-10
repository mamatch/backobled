from datetime import datetime

from pydantic import BaseModel
import enum
from fastapi import Query

from city import City


class Airport(BaseModel):
    name: str
    city: City
