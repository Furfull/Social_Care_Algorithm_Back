from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Notification(BaseModel):
    text: str
    user_id: int

