from abc import ABC, abstractmethod
from enum import Enum

from pydantic import BaseModel


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    NONBINARY = 3


class StudentData(BaseModel):
    index_number: int
    first_name: str
    last_name: str
    pesel: str
    gender: int
    address_city: str
    address_street: str
    address_zipcode: str


class CreateModifyStudentData(BaseModel):
    first_name: str
    last_name: str
    pesel: int
    gender: Gender
    address_city: str
    address_street: str
    address_zipcode: str


class StudentsBaseRepo(ABC):
    @abstractmethod
    async def get_student(self, index_number: int) -> StudentData | None:
        pass

    @abstractmethod
    async def get_students(self, last_name: str | None = None) -> list[StudentData]:
        pass

    @abstractmethod
    async def add_student(self, student_data: CreateModifyStudentData) -> None:
        pass

    @abstractmethod
    async def update_student(
        self, student_id: int, student_data: CreateModifyStudentData
    ) -> None:
        pass

    @abstractmethod
    def delete_student(self, student_id: int) -> None:
        pass


class StudentsBaseService(ABC):
    pass
