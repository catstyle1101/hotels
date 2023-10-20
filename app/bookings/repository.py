from sqlalchemy import select

from app.bookings.models import Bookings
from app.service import BaseRepository


class BookingRepository(BaseRepository):
    model = Bookings()
