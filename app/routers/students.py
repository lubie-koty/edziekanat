from typing import Annotated
from fastapi import APIRouter, Depends

from app.dependencies import get_students_service, get_users_repo
from app.students.types import StudentsBaseService, CreateStudentData, ModifyStudentData
from app.utils.auth import JWTBearer

router = APIRouter(
    prefix="/students",
    tags=["students"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(JWTBearer(Depends(get_users_repo)))],
)


@router.get("/")
async def get_students(
    students_service: Annotated[StudentsBaseService, Depends(get_students_service)],
    index_number: int | None = None,
    last_name: str | None = None,
    active: bool | None = None,
):
    return await students_service.get_students(
        index_number=index_number,
        last_name=last_name,
        active=active,
    )


@router.post("/")
async def create_student(
    students_service: Annotated[StudentsBaseService, Depends(get_students_service)],
    student_data: CreateStudentData,
):
    await students_service.add_student(student_data)


@router.patch("/{student_id}")
async def modify_student(
    students_service: Annotated[StudentsBaseService, Depends(get_students_service)],
    student_id: int,
    student_data: ModifyStudentData,
):
    await students_service.update_student(student_id, student_data)


@router.delete("/{student_id}")
async def delete_student(
    students_service: Annotated[StudentsBaseService, Depends(get_students_service)],
    student_id: int,
):
    await students_service.delete_student(student_id)
