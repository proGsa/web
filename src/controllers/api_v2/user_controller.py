from __future__ import annotations

import logging

from typing import Any

from fastapi import HTTPException
from fastapi import Request

from models.user import User
from schemas.auth import LoginRequest
from schemas.auth import LoginResponse
from schemas.user import UserCreate
from schemas.user import UserResponse
from schemas.user import UserUpdate
from services.user_service import AuthService
from services.user_service import UserService


logger = logging.getLogger(__name__)


class UserController:
    def __init__(self, user_service: UserService, auth_service: AuthService) -> None:
        self.user_service = user_service
        self.auth_service = auth_service
        logger.debug("Инициализация UserControllerV2")

    async def create_user(self, user_data: UserCreate) -> UserResponse:
        """
        Создает пользователя. Если is_admin=True, создается администратор через UserService,
        иначе обычный пользователь через AuthService.registrate.
        """
        try:
            # Хешируем пароль
            hashed_password = self.auth_service.get_password_hash(user_data.password)
            user_dict = user_data.dict()
            user_dict["password"] = hashed_password
            user = User(
                user_id=1,
                fio=user_data.fio,
                number_passport=user_data.number_passport,
                phone_number=user_data.phone_number,
                email=user_data.email,
                login=user_data.login,
                password=user_data.password,
                is_admin=user_data.is_admin
            )

            if user_data.is_admin:
                created_user = await self.user_service.add(user)
                logger.info("Администратор успешно создан: %s", created_user.login)
            else:
                created_user = await self.auth_service.registrate(user)
                logger.info("Пользователь успешно зарегистрирован: %s", created_user.login)

            return UserResponse(
                user_id=created_user.user_id,
                fio=created_user.fio,
                number_passport=created_user.number_passport,
                phone_number=created_user.phone_number,
                email=created_user.email,
                login=created_user.login,
                is_admin=created_user.is_admin
            )
        except ValueError as ve:
            logger.warning("Ошибка создания пользователя: %s", str(ve))
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            logger.error("Не удалось создать пользователя: %s", str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Internal server error")

    async def get_all_users(self) -> list[UserResponse]:
        try:
            users = await self.user_service.get_list()
            return [
                UserResponse(
                    user_id=u.user_id,
                    fio=u.fio,
                    number_passport=u.number_passport,
                    phone_number=u.phone_number,
                    email=u.email,
                    login=u.login,
                    is_admin=u.is_admin
                ) for u in users
            ]
        except Exception as e:
            logger.error("Ошибка при получении списка пользователей: %s", str(e), exc_info=True)
            raise HTTPException(status_code=500, detail=str(e))

    async def get_user_profile(self, user_id: int) -> UserResponse:
        user = await self.user_service.get_by_id(user_id)
        if not user:
            logger.warning("Пользователь ID %d не найден", user_id)
            raise HTTPException(status_code=404, detail="User not found")
        return UserResponse(
            user_id=user.user_id,
            fio=user.fio,
            number_passport=user.number_passport,
            phone_number=user.phone_number,
            email=user.email,
            login=user.login,
            is_admin=user.is_admin
        )

    async def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        user_old = await self.user_service.get_by_id(user_id)
        if not user_old:
            logger.warning("Пользователь ID %d не найден для обновления", user_id)
            raise HTTPException(status_code=404, detail="User not found")

        updated_data = user_data.dict(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(user_old, key, value)
        updated_user = await self.user_service.update(user_old)

        return UserResponse(
            user_id=updated_user.user_id,
            fio=updated_user.fio,
            number_passport=updated_user.number_passport,
            phone_number=updated_user.phone_number,
            email=updated_user.email,
            login=updated_user.login,
            is_admin=updated_user.is_admin
        )

    async def delete_user(self, user_id: int) -> None:
        user = await self.user_service.get_by_id(user_id)
        if not user:
            logger.warning("Пользователь ID %d не найден для удаления", user_id)
            raise HTTPException(status_code=404, detail="User not found")
        await self.user_service.delete(user_id)
        logger.info("Пользователь ID %d успешно удален", user_id)

    async def registrate(self, request: Request) -> dict[str, Any]:
        try:
            data = await request.json()
            user_data = UserCreate(**data)
            created_user = await self.create_user(user_data)
            token = self.auth_service.create_access_token(created_user)
            return {
                "access_token": token,
                "token_type": "bearer",
                "user_id": created_user.user_id,
                "message": "User registered successfully"
            }
        except Exception as e:
            logger.error("Ошибка регистрации пользователя: %s", str(e), exc_info=True)
            raise HTTPException(status_code=400, detail=str(e))

    async def login(self, credentials: LoginRequest) -> LoginResponse:
        try:
            user = await self.auth_service.authenticate(credentials.login, credentials.password)
            if not user:
                raise HTTPException(status_code=401, detail="Invalid login or password")

            token = self.auth_service.create_access_token(user)
            return LoginResponse(
                access_token=token,
                user_id=user.user_id,
                message="Login successful"
            )
        except Exception as e:
            logger.error("Ошибка авторизации пользователя: %s", str(e), exc_info=True)
            raise HTTPException(status_code=401, detail="Invalid login or password")
