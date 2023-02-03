from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()

students = [{"student_id": 1, "name": "Jens"}, {"student_id": 2, "name": "Bob"}]

class Student(BaseModel):
    student_id: int
    name: str

    @validator("student_id")
    def student_id_positive(cls, value):
        if value <= 0:
            raise ValueError(f"Expected positive price, received {value}")
        return value

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    name = q.upper()
    return {"item_id": item_id, "q": name}

@app.get("/name/{q}")
def read_name(q: str):
    return (q.upper())

@app.get("/students")
def read_students():
    return students

@app.post("/students/")
def create_student(student: Student):
    return student

@app.put("/students/{student_id}")
def save_student(student: Student):
    return student

@app.patch("/students/{student_id}")
def edit_student(student: Student):
    print(students[student.student_id-1].app)
    """ students[student.student_id]["name"].pop(student.student_id+1) """
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i in range(len(students)):
        if students[i]["student_id"] == student_id:
            del students[i]
            break
    print(students)
    return students