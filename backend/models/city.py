from datetime import datetime

from pydantic import BaseModel
import enum
from fastapi import Query
from country import Country


class City(BaseModel):
    name: str
    country: Country
