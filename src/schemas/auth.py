from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    login: str
    password: str


class LoginResponse(BaseModel):
    access_token: str 
    user_id: int
