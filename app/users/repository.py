from app.service.base import BaseRepository
from app.users.models import Users


class UserRepository(BaseRepository):
    model = Users
