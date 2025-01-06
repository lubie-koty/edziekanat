from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Student(Base):
    __tablename__ = "students"

    index_number: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    pesel: Mapped[str]
    gender: Mapped[int]
    address_city: Mapped[str]
    address_street: Mapped[str]
    address_zipcode: Mapped[str]
    active: Mapped[bool] = mapped_column(default=True)
