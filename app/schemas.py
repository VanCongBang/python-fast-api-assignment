from pydantic import BaseModel, EmailStr, constr
from typing import Optional, List
from enum import Enum

class UserBase(BaseModel):
    email: EmailStr
    username: constr(min_length=1, max_length=50)
    first_name: constr(min_length=1, max_length=50)
    last_name: constr(min_length=1, max_length=50)
    is_active: bool = True
    is_admin: bool = False
    company_id: Optional[int] = None

class UserCreate(UserBase):
    password: constr(min_length=8)

class User(UserBase):
    id: int
    tasks: List['Task'] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class CompanyBase(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: Optional[str] = None
    mode: constr(min_length=1, max_length=50)
    rating: Optional[float] = None

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int
    users: List[User] = []

    class Config:
        orm_mode = True

class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class TaskPriority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class TaskBase(BaseModel):
    summary: constr(min_length=1, max_length=100)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM

class TaskCreate(TaskBase):
    user_id: int

class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True