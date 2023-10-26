from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    name: str = Field(pattern=r"^[a-zA-Z0-9 ]+$")
    password: str = Field(pattern=r"^[a-zA-Z0-9_#.@&]+$")
    email: EmailStr
    user: str = Field(pattern=r"^[a-zA-Z0-9_]+$")
    born_date: str

class UserLogin(BaseModel):
    user: str = Field(pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(pattern=r"^[a-zA-Z0-9_#.@&]+$")