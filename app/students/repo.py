from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.students.models import Student
from app.students.types import (
    CreateStudentData,
    ModifyStudentData,
    StudentSortingType,
    StudentsBaseRepo,
    StudentData,
)


class StudentsRepo(StudentsBaseRepo):
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def get_students_by_filters(
        self,
        index_number: int | None = None,
        last_name: str | None = None,
        sorting: int | None = None,
        active: bool | None = None,
    ) -> list[StudentData]:
        async with self.db_session.begin():
            q = select(Student)
            if index_number:
                q = q.where(Student.index_number == index_number)
            if last_name:
                q = q.where(Student.last_name == last_name)
            if active is not None:
                q = q.where(Student.active == active)
            if sorting:
                match sorting:
                    case StudentSortingType.BY_INDEX.value:
                        q = q.order_by(Student.index_number)
                    case StudentSortingType.BY_LAST_NAME.value:
                        q = q.order_by(Student.last_name)
                    case StudentSortingType.BY_PESEL.value:
                        q = q.order_by(Student.pesel)
            result = (await self.db_session.execute(q)).scalars().all()
        return [
            StudentData(
                index_number=student.index_number,
                first_name=student.first_name,
                last_name=student.last_name,
                pesel=student.pesel,
                gender=student.gender,
                address_city=student.address_city,
                address_street=student.address_street,
                address_zipcode=student.address_zipcode,
            )
            for student in result
        ]

    async def add_student(self, student_data: CreateStudentData) -> None:
        async with self.db_session.begin():
            self.db_session.add(Student(**student_data.model_dump()))

    async def update_student(
        self, student_id: int, student_data: ModifyStudentData
    ) -> None:
        async with self.db_session.begin():
            q = select(Student).where(Student.index_number == student_id)
            existing_student = (await self.db_session.execute(q)).scalar_one()
            for key, new_value in student_data.model_dump(exclude_none=True).items():
                setattr(existing_student, key, new_value)
            await self.db_session.commit()

    async def delete_student(self, student_id: int) -> None:
        async with self.db_session.begin():
            q = select(Student).where(
                Student.index_number == student_id,
                Student.active == True,  # noqa
            )
            existing_student = (await self.db_session.execute(q)).scalar_one()
            existing_student.active = False
            await self.db_session.commit()
