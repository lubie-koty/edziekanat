from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.students.models import Student
from app.students.types import StudentsBaseRepo, StudentData


class StudentsRepo(StudentsBaseRepo):
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def get_student(self, index_number: int) -> StudentData | None:
        q = select(Student).where(Student.index_number == index_number)
        result = (await self.db_session.execute(q)).scalar()
        if not result:
            return None
        return StudentData(
            index_number=result.index_number,
            first_name=result.first_name,
            last_name=result.last_name,
            pesel=result.pesel,
            gender=result.gender,
            address_city=result.address_city,
            address_street=result.address_street,
            address_zipcode=result.address_zipcode,
        )

    async def get_students(self, last_name: str | None = None) -> list[StudentData]:
        q = select(Student)
        if last_name:
            q = q.where(Student.last_name == last_name)
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

    async def add_student(self, student_data: CreateModifyStudentData) -> None:
        pass
