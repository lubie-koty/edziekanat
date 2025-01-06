from typing import Annotated

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.students.repo import StudentsRepo
from app.students.service import StudentsService
from app.students.types import StudentsBaseRepo


async def get_db(request: Request):
    async_session = request.app.state.async_session
    async with async_session() as session:
        yield session
        await session.rollback()


async def get_students_repo(db_session: Annotated[AsyncSession, Depends(get_db)]):
    repo = StudentsRepo(db_session)
    return repo


async def get_students_service(
    students_repo: Annotated[StudentsBaseRepo, Depends(get_students_repo)],
):
    service = StudentsService(students_repo)
    return service
