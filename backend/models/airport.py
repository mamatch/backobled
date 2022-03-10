from datetime import datetime
from typing import List
from flight import Flight
from pydantic import BaseModel
import enum
from fastapi import Query

from city import City


class Airport(BaseModel):
    name: str
    city: City
    flights_from: List[Flight] # flights which go from this airport
    flights_to: List[Flight] # flights which go to this airport
