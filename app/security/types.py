from abc import ABC, abstractmethod

from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserData(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    password_hash: str


class CreateUserData(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class ModifyUserData(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    password: str | None = None


class UserLoginData(BaseModel):
    email: str
    password: str


class UsersBaseRepo(ABC):
    @abstractmethod
    async def get_user(self, email: str) -> UserData | None:
        pass

    @abstractmethod
    async def add_user(self, user_data: CreateUserData) -> None:
        pass

    @abstractmethod
    async def update_user(self, user_id: int, user_data: ModifyUserData) -> None:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        pass


class UsersBaseService(ABC):
    @abstractmethod
    async def login_user(self, email: str, password: str) -> TokenResponse:
        pass

    @abstractmethod
    async def create_user(self, user_data: CreateUserData) -> None:
        pass

    @abstractmethod
    async def update_user(self, user_id: int, user_data: ModifyUserData) -> None:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        pass
