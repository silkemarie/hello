from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, validator

app = FastAPI()

class Student(BaseModel):
    student_id: int
    name: str

    @validator("student_id")
    def student_id_positive(cls, value):
        if value <= 0:
            raise ValueError(f"Expected positive price, received {value}")
        return value

students = []

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


@app.post("/student/{student_id}")
def create_student(student: Student):
    students.append(student)
    return students


@app.put("/student/{student_id}")
def save_student(student_id: int, q: str):
    return {"id": student_id, "name": q}

@app.patch("/student/{student_id}")
def edit_student(student_id: int, q: str):
    
    return {"id": student_id, "name": q}

@app.delete("/student/{student_id}")
def delete_student(student_id: int)->list:
    students.remove(student_id)
    return students

#to do: watch videoes, write tests, commit often
#add pydantic import 