from typing import Annotated
from fastapi import APIRouter, Depends

from app.dependencies import get_users_service
from app.security.types import (
    CreateUserData,
    ModifyUserData,
    UserLoginData,
    UsersBaseService,
)

router = APIRouter(
    prefix="/security",
    tags=["security"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
async def login(
    users_service: Annotated[UsersBaseService, Depends(get_users_service)],
    login_data: UserLoginData,
):
    return await users_service.login_user(
        email=login_data.email, password=login_data.password
    )


@router.post("/register")
async def register(
    users_service: Annotated[UsersBaseService, Depends(get_users_service)],
    user_data: CreateUserData,
):
    await users_service.create_user(user_data)


@router.patch("/users/{user_id}")
async def modify_user(
    users_service: Annotated[UsersBaseService, Depends(get_users_service)],
    user_id: int,
    user_data: ModifyUserData,
):
    await users_service.update_user(user_id, user_data)


@router.delete("/users/{user_id}")
async def delete_user(
    users_service: Annotated[UsersBaseService, Depends(get_users_service)],
    user_id: int,
):
    await users_service.delete_user(user_id)
