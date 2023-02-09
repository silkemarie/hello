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


""" class UserBase(BaseModel):
    email: str """

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str 


class UserCreate(User):
    password: str
"""

class User(User):
    id: int
    is_active: bool
    items: List[Item] = []
        
    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str
"""

class StudentBase(BaseModel):
    first_name: str
    last_name: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    student_id: int

    class Config:
        orm_mode = True
