from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.security.models import User
from app.security.types import (
    CreateUserData,
    ModifyUserData,
    UsersBaseRepo,
    UserData,
)
from app.utils.auth import get_password_hash


class UsersRepo(UsersBaseRepo):
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def get_user(self, email: str) -> UserData | None:
        async with self.db_session.begin():
            q = select(User).where(
                User.email == email,
                User.active == True,  # noqa
            )
            result = (await self.db_session.execute(q)).scalar_one_or_none()
        if not result:
            return None
        return UserData(
            user_id=result.user_id,
            first_name=result.first_name,
            last_name=result.last_name,
            email=result.email,
            password_hash=result.password_hash,
        )

    async def add_user(self, user_data: CreateUserData) -> None:
        async with self.db_session.begin():
            self.db_session.add(
                User(
                    first_name=user_data.first_name,
                    last_name=user_data.last_name,
                    email=user_data.email,
                    password_hash=get_password_hash(user_data.password),
                )
            )

    async def update_user(self, user_id: int, user_data: ModifyUserData) -> None:
        async with self.db_session.begin():
            q = select(User).where(User.user_id == user_id)
            existing_user = (await self.db_session.execute(q)).scalar_one()
            if first_name := user_data.first_name:
                existing_user.first_name = first_name
            if last_name := user_data.last_name:
                existing_user.last_name = last_name
            if email := user_data.email:
                existing_user.email = email
            if password := user_data.password:
                existing_user.password_hash = get_password_hash(password)
            await self.db_session.commit()

    async def delete_user(self, user_id: int) -> None:
        async with self.db_session.begin():
            q = select(User).where(
                User.user_id == user_id,
                User.active == True,  # noqa
            )
            existing_user = (await self.db_session.execute(q)).scalar_one()
            existing_user.active = False
            await self.db_session.commit()
