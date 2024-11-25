from sqlalchemy.ext.asyncio import AsyncSession

from app.students.types import StudentsBaseRepo


class StudentsRepo(StudentsBaseRepo):
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session
