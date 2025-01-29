from typing import Annotated

from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from app.students.repo import StudentsRepo
from app.students.service import StudentsService
from app.students.types import StudentsBaseRepo
from app.security.repo import UsersRepo
from app.security.service import UsersService
from app.security.types import UsersBaseRepo
from app.utils.auth import JWTBearer


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


async def get_users_repo(db_session: Annotated[AsyncSession, Depends(get_db)]):
    repo = UsersRepo(db_session)
    return repo


async def get_users_service(
    users_repo: Annotated[UsersBaseRepo, Depends(get_users_repo)],
):
    service = UsersService(users_repo)
    return service


async def get_jwt_bearer(
    users_repo: Annotated[UsersBaseRepo, Depends(get_users_repo)],
    request: Request,
) -> HTTPAuthorizationCredentials:
    jwt_bearer = JWTBearer(users_repo)
    return await jwt_bearer(request)
