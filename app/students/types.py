from abc import ABC, abstractmethod
from enum import Enum, IntEnum
from typing import Annotated

from pydantic import AfterValidator, BaseModel

from app.utils.validators import check_pesel


class Gender(IntEnum):
    MALE = 1
    FEMALE = 2
    NONBINARY = 3


class StudentData(BaseModel):
    index_number: int
    first_name: str
    last_name: str
    pesel: Annotated[str, AfterValidator(check_pesel)]
    gender: int
    address_city: str
    address_street: str
    address_zipcode: str


class CreateStudentData(BaseModel):
    first_name: str
    last_name: str
    pesel: Annotated[str, AfterValidator(check_pesel)]
    gender: Gender
    address_city: str
    address_street: str
    address_zipcode: str


class ModifyStudentData(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    pesel: Annotated[str, AfterValidator(check_pesel)] | None = None
    gender: Gender | None = None
    address_city: str | None = None
    address_street: str | None = None
    address_zipcode: str | None = None


class StudentSortingType(Enum):
    BY_INDEX = 0
    BY_LAST_NAME = 1
    BY_PESEL = 2


class StudentsBaseRepo(ABC):
    @abstractmethod
    async def get_students_by_filters(
        self,
        index_number: int | None = None,
        last_name: str | None = None,
        sorting: int | None = None,
        active: bool | None = None,
    ) -> list[StudentData]:
        pass

    @abstractmethod
    async def add_student(self, student_data: CreateStudentData) -> None:
        pass

    @abstractmethod
    async def update_student(
        self, student_id: int, student_data: ModifyStudentData
    ) -> None:
        pass

    @abstractmethod
    async def delete_student(self, student_id: int) -> None:
        pass


class StudentsBaseService(ABC):
    @abstractmethod
    async def get_students(
        self,
        index_number: int | None = None,
        last_name: str | None = None,
        sorting: int | None = None,
        active: bool | None = None,
    ) -> list[StudentData]:
        pass

    @abstractmethod
    async def add_student(self, student_data: CreateStudentData) -> None:
        pass

    @abstractmethod
    async def update_student(
        self, student_id: int, student_data: ModifyStudentData
    ) -> None:
        pass

    @abstractmethod
    async def delete_student(self, student_id: int) -> None:
        pass
