from __future__ import annotations

from typing import ClassVar

from pydantic import BaseModel
from pydantic import field_validator


class City(BaseModel):
    MAX_NAME_LENGTH: ClassVar[int] = 50
    city_id: int
    name: str
    class Config:
        validate_by_name = True

    @field_validator('city_id')
    @classmethod
    def check_city_id(cls, value: int) -> int:
        if value <= 0:
            raise ValueError('city_id должен быть положительным числом')
        return value
    
    @field_validator('name')
    @classmethod
    def validate_check_name_length(cls, value: str) -> str:
        if len(value) < 1:
            raise ValueError('name должно быть длиннее')
        if len(value) > cls.MAX_NAME_LENGTH:
            raise ValueError('name должно быть короче')
        return value

    