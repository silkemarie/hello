from typing import Union

from fastapi import FastAPI

app = FastAPI()

student = []

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
def create_student(student_id: int, q: str):
    student.append({"id": student_id, "name": q})
    return student


@app.put("/student/{student_id}")
def save_student(student_id: int, q: str):
    return {"id": student_id, "name": q}

@app.patch("/student/{student_id}")
def edit_student(student_id: int, q: str):
    
    return {"id": student_id, "name": q}

@app.delete("/student/{student_id}")
def delete_student(student_id: int)->list:
    student.remove(student_id)
    return student

#to do: watch videoes, write tests, commit often