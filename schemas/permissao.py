from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Permission(BaseModel):
    facebook: int
    instagram: int
    twitter: int
    spotify: int
    tiktok: int

class PermissionFacebookUpdateState(BaseModel):
    id: int
    facebook: int


class PermissionFacebookGetState(BaseModel):
    id: int
    facebook: int
