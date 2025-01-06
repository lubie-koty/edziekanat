from datetime import timedelta

from fastapi.exceptions import HTTPException
from fastapi import status

from app.internal.config import settings
from app.security.types import (
    CreateUserData,
    ModifyUserData,
    UsersBaseRepo,
    UsersBaseService,
    TokenResponse,
)
from app.utils.auth import create_access_token, get_password_hash, verify_password


class UsersService(UsersBaseService):
    def __init__(self, users_repo: UsersBaseRepo):
        self.users_repo = users_repo

    async def login_user(self, email: str, password: str) -> TokenResponse:
        user = await self.users_repo.get_user(email)
        if not user:
            raise HTTPException(
                status.HTTP_401_UNAUTHORIZED, detail="User does not exist"
            )
        if not verify_password(get_password_hash(password), user.password_hash):
            raise HTTPException(
                status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
            )
        access_token = create_access_token(
            email, timedelta(minutes=settings.jwt_access_token_expire_minutes)
        )
        return TokenResponse(access_token=access_token, token_type="Bearer")

    async def create_user(self, user_data: CreateUserData) -> None:
        user = await self.users_repo.get_user(user_data.email)
        if user:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                detail=f"User {user_data.email} already exists",
            )
        await self.users_repo.add_user(user_data)

    async def update_user(self, user_id: int, user_data: ModifyUserData) -> None:
        try:
            await self.users_repo.update_user(user_id, user_data)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def delete_user(self, user_id: int) -> None:
        try:
            await self.users_repo.delete_user(user_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
