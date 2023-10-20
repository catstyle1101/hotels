from typing import Mapping, Sequence
from sqlalchemy import RowMapping, select

from app.database import async_session_maker, Base
from app.exceptions import ModelNotDefinedError


class BaseRepository:
    model: Base | None = None

    @classmethod
    async def find_one_or_none(
        cls, **filter_by: Mapping[str, str]) -> RowMapping | None:
        if cls.model is None:
            raise ModelNotDefinedError
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(
        cls, **filter_by: Mapping[str, str]) -> Sequence[RowMapping]:
        if cls.model is None:
            raise ModelNotDefinedError
        async with async_session_maker() as session:
            query = (
                select(
                    cls.model.__table__.columns,
                )
                .filter_by(**filter_by)
            )
            result = await session.execute(query)
            return result.mappings().all()
