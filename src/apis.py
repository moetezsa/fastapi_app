import fastapi
from sqlalchemy.orm import Session
import src.services as services
import src.schemas as schemas
from typing import List


app = fastapi.FastAPI()
services.create_tables()

@app.post("/api/students/", response_model=schemas.Student)
async def create_student(
        student: schemas.CreateStudent,
        db: Session = fastapi.Depends(services.get_db),
        ):
    return await services.create_student(student=student, db=db)


@app.get("/api/students/",
         response_model=List[schemas.Student],
         )
async def get_students(db: Session = fastapi.Depends(services.get_db),
                       ):
    return await services.get_students(db=db)


@app.get("/api/students/{id}/", response_model=schemas.Student)
async def get_student(id: int,
                      db: Session = fastapi.Depends(services.get_db),
                      ):
    student = await services.get_student(id=id, db=db)
    if student is None:
        raise fastapi.HTTPException(status_code=404, detail="Student does not exist")
    return student


@app.delete("/api/students/{id}/")
async def delete_student(id: int,
                         db: Session = fastapi.Depends(services.get_db),
                         ):
    student = await services.get_student(id=id, db=db)
    if student is None:
        raise fastapi.HTTPException(status_code=404, detail="Student does not exist")
    await services.delete_student(id=id, db=db)
    return "Student deleted"


@app.put("/api/students/{id}", response_model=schemas.Student)
async def update_student(id: int,
                         student_data: schemas.CreateStudent,
                         db: Session = fastapi.Depends(services.get_db),
                         ):
    student = await services.get_student(id=id, db=db)
    if student is None:
        raise fastapi.HTTPException(status_code=404, detail="Student does not exist")
    return await services.update_student(id=id, student_data=student_data, db=db)
