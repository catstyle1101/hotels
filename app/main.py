from datetime import date
from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, Field

from app.bookings.router import router as router_bookings

app = FastAPI()

app.include_router(router_bookings)

class SHotel(BaseModel):
    address: str
    name: str
    stars: int = Field(None, ge=0, le=5)


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: int = Query(None, ge=1, le=5),
        has_spa: bool = Query(None),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


@app.get("/hotels/{hotel_id}")
async def get_hotels(
    search_args: HotelsSearchArgs = Depends(),
) -> list[SHotel]:
    hotels = [
        SHotel(
            address="Ул. Гагарина, 1, Алтай",
            name="Super Spa Resort",
            stars=5,
        )
    ]
    return hotels


class SBookingPOST(BaseModel):
    id: int
    date_from: date
    date_to: date


@app.post("/bookings")
async def add_booking(booking: SBookingPOST) -> SHotel:
    return SHotel(**booking)
