from pydantic import BaseModel
import datetime as dt


class BaseStudent(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: dt.date
    age: int


class Student(BaseStudent):
    id: int

    class Config:
        from_attributes = True


class CreateStudent(BaseStudent):
    pass
