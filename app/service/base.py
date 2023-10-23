from typing import Sequence
from sqlalchemy import RowMapping, insert, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase

from app.database import async_session_maker
from app.exceptions import ModelNotDefinedError
from app.logger import logger


class BaseRepository:
    model: DeclarativeBase | None = None

    @classmethod
    async def find_one_or_none(
        cls, **filter_by: str | int) -> RowMapping | None:
        if cls.model is None:
            raise ModelNotDefinedError
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(
        cls, **filter_by: str | int) -> Sequence[RowMapping]:
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

    @classmethod
    async def add(cls, **data: str | int) -> RowMapping | None:
        try:
            stmt = insert(cls.model).values(**data).returning(cls.model.id)
            async with async_session_maker() as session:
                result = await session.execute(stmt)
                await session.commit()
                return result.mappings().first()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database Exc: Cannot insert data into table"
            elif isinstance(e, Exception):
                msg = "Unknown Exc: Cannot insert data into table"

            logger.error(
                msg, extra={"table": cls.model.__tablename__}, exc_info=True)
            return None
