from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Form(BaseModel):
    pcd: str
    gender: str
    sexuality: str
    ethny: str
    money: str

