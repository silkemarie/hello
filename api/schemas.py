from typing import List, Union
from pydantic import BaseModel, validator

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    pass 

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    student_id: int
    name: str

    @validator("student_id")
    def student_id_positive(cls, value):
        if value <= 0:
            raise ValueError(f"Expected positive price, received {value}")
        return value

class StudentCreate(StudentBase):
    name: str

class Student(StudentBase):

    class Config:
        orm_mode = True
