from typing import List, Union
from pydantic import BaseModel


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
    username: str
    email: str
    full_name: Union[str, None] = None


class UserCreate(UserBase):
    username: str
    email: str
    password: str


class UserInDB(UserCreate):
    hashed_password: str 

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
        
    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str


class StudentBase(BaseModel):
    first_name: str
    last_name: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    student_id: int

    class Config:
        orm_mode = True
