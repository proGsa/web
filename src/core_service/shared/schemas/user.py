from __future__ import annotations

from pydantic import BaseModel
from pydantic import EmailStr


class UserBase(BaseModel):
    fio: str
    number_passport: str
    phone_number: str
    email: EmailStr
    login: str


class UserCreate(UserBase):
    password: str
    is_admin: bool = False


class UserUpdate(BaseModel):
    fio: str | None
    number_passport: str | None
    phone_number: str | None
    email: EmailStr | None
    is_admin: bool | None


class UserResponse(UserBase):
    user_id: int
    is_admin: bool

    class Config:
        orm_mode = True


class UsersResponse(BaseModel):
    users: list[UserResponse]


class LoginRequest(BaseModel):
    login: str  
    password: str