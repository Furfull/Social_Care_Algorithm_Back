from datetime import date
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class Contact(BaseModel):
    name: str = Field(pattern=r"^[a-zA-Z0-9 ]{15}$")
    number: str
    user_id: int

class ContactShow(BaseModel):
    id: int
    name: str
    number: str