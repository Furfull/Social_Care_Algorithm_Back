from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Feed(BaseModel):
    text: str = ""
    overview: str = ""
    positive: str = ""
    negative: str = ""
    neutral: str = ""

