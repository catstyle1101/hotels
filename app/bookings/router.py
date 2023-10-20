from typing import Sequence
from fastapi import APIRouter
from sqlalchemy import RowMapping

from app.bookings.repository import BookingRepository
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("", response_model=list[SBooking])
async def get_bookings():
    return await BookingRepository.find_all()
