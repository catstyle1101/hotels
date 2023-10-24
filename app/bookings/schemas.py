from datetime import date
from typing import Annotated, Optional
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
        from_attributes = True


class SBookingInfo(SBooking):
    image_id: int
    name: str
    description: Optional[str]
    services: list[str]

    class Config:
        from_attributes = True


class SNewBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
