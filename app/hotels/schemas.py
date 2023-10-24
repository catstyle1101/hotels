from typing import List

from pydantic import BaseModel


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int

    class Config:
        from_atttibutes = True


class SHotelInfo(SHotel):
    rooms_left: int

    class Config:
        from_atttibutes = True
