from src import database, models, schemas
from sqlalchemy.orm import session
from typing import List


def create_tables():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_student(
        student: schemas.CreateStudent,
        db: session,
) -> schemas.Student:
    student = models.Student(**student.dict())
    db.add(student)
    db.commit()
    db.refresh(student)
    return schemas.Student.from_orm(student)


async def get_students(db: session) -> List[schemas.Student]:
    students = db.query(models.Student).all()
    return list(map(schemas.Student.from_orm, students))


async def get_student(id: int, db: session) -> schemas.Student:
    student = db.query(models.Student).filter(models.Student.id == id).first()
    return student


async def delete_student(id: int, db: session):
    db.query(models.Student).filter(models.Student.id == id).delete()
    db.commit()


async def update_student(id: int, student_data: schemas.CreateStudent, db: session) -> schemas.Student:
    student = db.query(models.Student).filter(models.Student.id == id).first()
    student.first_name = student_data.first_name
    student.last_name = student_data.last_name
    student.date_of_birth = student_data.date_of_birth
    student.age = student_data.age
    db.commit()
    db.refresh(student)
    return schemas.Student.from_orm(student)
