from app.students.types import (
    CreateStudentData,
    ModifyStudentData,
    StudentsBaseRepo,
    StudentsBaseService,
    StudentData,
)


class StudentsService(StudentsBaseService):
    def __init__(self, students_repo: StudentsBaseRepo):
        self.students_repo = students_repo

    async def get_students(
        self,
        index_number: int | None = None,
        last_name: str | None = None,
        active: bool | None = None,
    ) -> list[StudentData]:
        students_list = await self.students_repo.get_students_by_filters(
            index_number, last_name, active
        )
        return students_list

    async def add_student(self, student_data: CreateStudentData) -> None:
        await self.students_repo.add_student(student_data)

    async def update_student(
        self, student_id: int, student_data: ModifyStudentData
    ) -> None:
        await self.students_repo.update_student(student_id, student_data)

    async def delete_student(self, student_id: int) -> None:
        await self.students_repo.delete_student(student_id)
