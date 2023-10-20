from datetime import date
from typing import Annotated
from pydantic import BaseModel, Field


class SBooking(BaseModel):
    id: int
    room_id: Annotated[int, Field(ge=0)]
    user_id: Annotated[int, Field(ge=0)]
    date_from: date
    date_to: date
    price: Annotated[int, Field(ge=0)]
    total_days: Annotated[int, Field(ge=0)]
    total_cost: Annotated[int, Field(ge=0)]

    class Config:
        orm_mode = True
