from abc import ABC, abstractmethod
from enum import Enum

from pydantic import BaseModel


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    NONBINARY = 3


class UserData(BaseModel):
    index_number: int
    first_name: str
    last_name: str
    pesel: int
    gender: Gender
    address_city: str
    address_street: str
    address_zipcode: str


class CreateModifyUserData(BaseModel):
    first_name: str
    last_name: str
    pesel: int
    gender: Gender
    address_city: str
    address_street: str
    address_zipcode: str


class StudentsBaseRepo(ABC):
    @abstractmethod
    def get_student(
        self,
        index_number: int | None,
        last_name: str | None,
    ) -> UserData | None:
        pass

    @abstractmethod
    def get_students(self) -> list[UserData]:
        pass

    @abstractmethod
    def add_student(self, student_data: CreateModifyUserData) -> None:
        pass

    @abstractmethod
    def update_student(
        self, student_id: int, student_data: CreateModifyUserData
    ) -> None:
        pass

    @abstractmethod
    def delete_student(self, student_id: int) -> None:
        pass


class StudentsBaseService(ABC):
    pass
