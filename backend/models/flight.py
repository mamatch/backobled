from datetime import datetime

from pydantic import BaseModel
import enum
from fastapi import Query
from user import User
from airport import Airport


class Flight(BaseModel):
    user: User
    go_airport: Airport
    arrive_airport: Airport
    capacity: float
    price_per_kg: float
    date: datetime
    specific_information: str
