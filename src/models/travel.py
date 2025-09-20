from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

from models.accommodation import Accommodation
from models.entertainment import Entertainment
from models.user import User


class Travel(BaseModel):
    travel_id: int
    status: str
    # users: User | None = Field(default=None, description="ID пользователя")
    users: list[User] = Field(default_factory=list, description="Список пользователей")
    entertainments: list[Entertainment] = Field(default_factory=list, description="Список развлечения")
    accommodations: list[Accommodation] = Field(default_factory=list, description="Список размещения")

    class Config:
        validate_by_name = True
        
    @field_validator('travel_id')
    @classmethod
    def check_travel_id(cls, value: int) -> int:
        if value <= 0:
            raise ValueError('travel_id должен быть положительным числом')
        return value

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: str) -> str:
        allowed_types = {'В процессе', 'Завершен', 'Отменен'}
        if v not in allowed_types:
            raise ValueError(f'e_type должен быть одним из следующих: {", ".join(allowed_types)}')
        return v

    @field_validator('users')
    @classmethod
    def check_users(cls, value: list[User]) -> list[User]:
        if value is not None:
            if not isinstance(value, list):
                raise ValueError("users должен быть списком")
            if not value:
                raise ValueError("Список users не должен быть пустым")
            if not all(isinstance(item, User) for item in value):
                raise ValueError("Bce элементы users должны быть экземплярами User")

        return value
    # @field_validator('users')
    # @classmethod
    # def check_users(cls, value: User | None) -> User | None:
    #     if value is not None and not isinstance(value, User):
    #         raise ValueError('route должен быть экземпляром User')
    #     return value

    @field_validator('entertainments')
    @classmethod
    def check_entertainments(cls, value: list[Entertainment]) -> list[Entertainment]:
        if value is not None:
            if not isinstance(value, list):
                raise ValueError("entertainments должен быть списком")
            if not value:
                raise ValueError("Список entertainments не должен быть пустым")
            if not all(isinstance(item, Entertainment) for item in value):
                raise ValueError("Bce элементы entertainments должны быть экземплярами Entertainment")

        return value

    @field_validator('accommodations')
    @classmethod
    def check_accommodations(cls, value: list[Accommodation]) -> list[Accommodation]:
        if value is not None:
            if not isinstance(value, list):
                raise ValueError("accommodation должен быть списком")
            if not value:
                raise ValueError("Список accommodation не должен быть пустым")
            if not all(isinstance(item, Accommodation) for item in value):
                raise ValueError("Bce элементы accommodation должны быть экземплярами Accommodation")

        return value