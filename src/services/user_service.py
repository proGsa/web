from __future__ import annotations

import logging

from datetime import datetime
from datetime import timedelta
from typing import Any

import bcrypt

from jose import jwt

from abstract_repository.iuser_repository import IUserRepository
from abstract_service.user_service import IAuthService
from abstract_service.user_service import IUserService
from models.user import User
from settings import settings


logger = logging.getLogger(__name__)

# Конфигурация
secret_key = settings.get_secret_key()
algorithm = settings.ALGORITHM
session_timeout = settings.SESSION_TIMEOUT


class UserService(IUserService):
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository
        logger.debug("UserService инициализирован")

    async def add(self, user: User) -> User:
        try:
            logger.debug("Добавление администратора с логином %s", user)
            user = await self.repository.add(user)
        except (Exception):
            logger.error("Администратора с логином %s уже существует.", user.login)
            raise ValueError("Администратор c таким ID уже существует.")
        return user

    async def get_by_id(self, user_id: int) -> User | None:
        logger.debug("Получение пользователя по ID %d", user_id)
        return await self.repository.get_by_id(user_id)

    async def get_list(self) -> list[User]:
        logger.debug("Получение списка всех пользователей")
        return await self.repository.get_list()

    async def update(self, updated_user: User) -> User:
        try:
            logger.debug("Обновление пользователя с ID %d", updated_user.user_id)
            await self.repository.update(updated_user)
        except (Exception):
            logger.error("Пользователь с ID %d не найден.", updated_user.user_id)
            raise ValueError("Пользователь не найден.")
        return updated_user

    async def delete(self, user_id: int) -> None:
        try:
            logger.debug("Удаление пользователя с ID %d", user_id)
            await self.repository.delete(user_id)
        except (Exception):
            logger.error("Пользователь с ID %d не найден.", user_id)
            raise ValueError("Пользователь не найден.")


class AuthService(IAuthService):
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository
        logger.debug("AuthService инициализирован")

    async def registrate(self, user: User) -> User:
        user.password = self.get_password_hash(user.password)
        
        logger.debug("Регистрация пользователя с логином %s", user)
        try:
            await self.repository.add(user)
        except Exception as e:
            logger.error("Ошибка регистрации пользователя %s: %s", user.login, str(e))
            raise ValueError("Пользователь с таким логином уже существует")
        
        return user

    async def authenticate(self, login: str, password: str) -> User | None:
        user = await self.repository.get_by_login(login)
        if not user:
            logger.info("Пользователь %s не найден", login)
            return None
        if not self.verify_password(password, user.password):
            logger.info("Неверный пароль для пользователя %s", login)
            return None
            
        return user
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str | bytes) -> bool:
        try:
            plain_bytes = plain_password.encode('utf-8')
            hash_bytes = hashed_password.encode('utf-8') if isinstance(hashed_password, str) else hashed_password
            return bcrypt.checkpw(plain_bytes, hash_bytes)
        except Exception as e:
            logger.error(f"Password verification failed: {e!s}")
            return False
    
    @staticmethod
    def create_access_token(user: User) -> str:
        expires_delta = timedelta(minutes=session_timeout)
        expire = datetime.utcnow() + expires_delta
        
        to_encode = {
            "sub": str(user.user_id),
            "login": user.login,
            "is_admin": user.is_admin,
            "exp": expire
        }
        return jwt.encode(to_encode, secret_key, algorithm=algorithm)
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def decode_token(token: str) -> dict[str, Any]:
        """Декодирование JWT токена"""
        return jwt.decode(token, secret_key, algorithms=[algorithm])