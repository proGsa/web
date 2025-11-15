from __future__ import annotations

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from schemas.user import UserCreate
from schemas.user import UserResponse
from schemas.user import UsersResponse
from schemas.user import UserUpdate
from service_locator import ServiceLocatorV2
from service_locator import get_service_locator_v2


user_router = APIRouter(prefix="/users", tags=["users"])
get_sl_dep = Depends(get_service_locator_v2)


@user_router.post("/", response_model=UserResponse, responses={
    400: {"description": "Неверный запрос"},
    500: {"description": "Внутренняя ошибка сервера"},
})
async def create_user(user: UserCreate, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        created_user = await service_locator.get_user_contr().create_user(user)
        return created_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.get("/", response_model=UsersResponse, responses={
    404: {"description": "Пользователи не найдены"},
    500: {"description": "Внутренняя ошибка сервера"},
})
async def get_all_users(service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        users = await service_locator.get_user_contr().get_all_users()
        if not users:
            raise HTTPException(status_code=404, detail="Users not found")
        return {"users": users}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@user_router.get("/{user_id}", response_model=UserResponse, responses={
    404: {"description": "Пользователь не найдены"},
    500: {"description": "Внутренняя ошибка сервера"},
})
async def get_user(user_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        user = await service_locator.get_user_contr().get_user_profile(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@user_router.put("/{user_id}", response_model=UserResponse, responses={
    400: {"description": "Неверный запрос"},
    404: {"description": "Пользователи не найдены"},
    500: {"description": "Внутренняя ошибка сервера"},
})
async def update_user(user_id: int, user: UserUpdate, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        updated_user = await service_locator.get_user_contr().update_user(user_id, user)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, responses={
    404: {"description": "Пользователи не найдены"},
    500: {"description": "Внутренняя ошибка сервера"},
})
async def delete_user(user_id: int, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        await service_locator.get_user_contr().delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
