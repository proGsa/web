from __future__ import annotations

import logging

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from ...shared.schemas.auth import LoginRequest
from ...shared.schemas.auth import LoginResponse
from ...service_locator import ServiceLocatorV2
from ...service_locator import get_service_locator_v2


logger = logging.getLogger(__name__)
router = APIRouter(prefix="/login", tags=["authentication"])
get_sl_dep = Depends(get_service_locator_v2)


@router.post(
    "",
    response_model=LoginResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        401: {"description": "Invalid login or password"},
        500: {"description": "Internal server error"},
    },
)
async def login_user(credentials: LoginRequest, service_locator: ServiceLocatorV2 = get_sl_dep):
    try:
        return await service_locator.get_user_contr().login(credentials)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid login or password")
    except Exception as e:
        logger.error(f"Ошибка при логине: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
