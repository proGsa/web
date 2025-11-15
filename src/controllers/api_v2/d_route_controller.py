from __future__ import annotations

import logging

from typing import Any

from fastapi import HTTPException

from models.directory_route import DirectoryRoute
from schemas.directory_route import DirectoryRouteCreate
from schemas.directory_route import DirectoryRouteResponse
from schemas.directory_route import DirectoryRouteResponseOut
from services.city_service import CityService
from services.directory_route_service import DirectoryRouteService


logger = logging.getLogger(__name__)


class DirectoryRouteController:
    def __init__(self, directory_route_service: DirectoryRouteService, city_service: CityService) -> None:
        self.directory_route_service = directory_route_service
        self.city_service = city_service
        logger.debug("Инициализация DirectoryRouteController")

    async def create_new_d_route(self, d_route: DirectoryRouteCreate) -> DirectoryRouteResponse:
        """Создание нового справочного маршрута"""
        try:
            departure_city = await self.city_service.get_by_id(d_route.departure_city)
            destination_city = await self.city_service.get_by_id(d_route.destination_city)

            if not departure_city or not destination_city:
                raise HTTPException(status_code=404, detail="One or both cities not found")

            d_route = DirectoryRoute(
                d_route_id=1,
                type_transport=d_route.type_transport,
                cost=d_route.cost,
                distance=d_route.distance,
                departure_city=departure_city,
                destination_city=destination_city
            )

            await self.directory_route_service.add(d_route)
            logger.info("Справочный маршрут успешно создан: %s", d_route)

            return DirectoryRouteResponseOut(
                id=d_route.d_route_id,
                type_transport=d_route.type_transport,
                cost=d_route.cost,
                distance=d_route.distance,
                departure_city=departure_city.name,
                destination_city=destination_city.name,
            )

        except HTTPException:
            raise
        except Exception as e:
            logger.error("Ошибка при создании справочного маршрута: %s", str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Error creating directory route")

    async def update_d_route(self, d_route_id: int, d_route_data):
        """
        PUT — полное обновление маршрута
        """
        try:
            departure_city = await self.city_service.get_by_id(d_route_data.departure_city)
            destination_city = await self.city_service.get_by_id(d_route_data.destination_city)

            if not departure_city or not destination_city:
                raise HTTPException(status_code=404, detail="One or both cities not found")
            d_route = DirectoryRoute(
                d_route_id=d_route_id,
                type_transport=d_route_data.type_transport,
                cost=d_route_data.cost,
                distance=d_route_data.distance,
                departure_city=departure_city,
                destination_city=destination_city
            )
            updated = await self.directory_route_service.update(d_route)

            logger.info("Справочный маршрут ID %d полностью обновлен", d_route_id)
            return DirectoryRouteResponseOut(
                id=updated.d_route_id,
                type_transport=updated.type_transport,
                cost=updated.cost,
                distance=updated.distance,
                departure_city=updated.departure_city.name,
                destination_city=updated.destination_city.name
            )

        except Exception as e:
            logger.error("Ошибка при полном обновлении маршрута ID %d: %s", d_route_id, str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Error updating directory route")

    async def partial_update_d_route(self, d_route_id: int, d_route_data):
        try:
            existing = await self.directory_route_service.get_by_id(d_route_id)
            if not existing:
                raise HTTPException(status_code=404, detail="Directory route not found")

            if not d_route_data.type_transport:
                raise HTTPException(status_code=400, detail="Field 'type_transport' is required for partial update")

            updated = await self.directory_route_service.change_transport(
                d_route_id,
                new_transport=d_route_data.type_transport
            )

            logger.info("Тип транспорта для маршрута ID %d изменен на '%s'", d_route_id, d_route_data.type_transport)
            return DirectoryRouteResponseOut(
                id=d_route_id,
                type_transport=updated.type_transport,
                cost=updated.cost,
                distance=updated.distance,
                departure_city=updated.departure_city.name,
                destination_city=updated.destination_city.name
            )

        except HTTPException:
            raise
        except Exception as e:
            logger.error("Ошибка при частичном обновлении маршрута ID %d: %s", d_route_id, str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Error partially updating directory route")

    async def get_d_route_details(self, d_route_id: int) -> DirectoryRouteResponse | None:
        """Получение маршрута по ID"""
        try:
            d_route = await self.directory_route_service.get_by_id(d_route_id)
            if not d_route:
                return None

            logger.info("Справочный маршрут ID %d найден", d_route_id)
            return DirectoryRouteResponseOut(
                id=d_route.d_route_id,
                type_transport=d_route.type_transport,
                cost=d_route.cost,
                distance=d_route.distance,
                departure_city=d_route.departure_city.name,
                destination_city=d_route.destination_city.name,
            )

        except Exception as e:
            logger.error("Ошибка при получении информации о маршруте ID %d: %s", d_route_id, str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Error fetching directory route details")

    async def get_all_d_routes(self) -> dict[str, Any]:
        """Получение всех маршрутов"""
        try:
            d_routes = await self.directory_route_service.get_list()
            logger.info("Получено %d справочных маршрутов", len(d_routes))

            return [
                    DirectoryRouteResponseOut(
                        id=r.d_route_id,
                        type_transport=r.type_transport,
                        cost=r.cost,
                        distance=r.distance,
                        departure_city=r.departure_city.name,
                        destination_city=r.destination_city.name,
                    )
                    for r in d_routes
                ]

        except Exception as e:
            logger.error("Ошибка при получении списка маршрутов: %s", str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Error fetching directory routes")

    async def delete_d_route(self, d_route_id: int) -> None:
        """Удаление маршрута"""
        try:
            await self.directory_route_service.delete(d_route_id)
            logger.info("Справочный маршрут ID %d успешно удален", d_route_id)
        except Exception as e:
            logger.error("Ошибка при удалении маршрута ID %d: %s", d_route_id, str(e), exc_info=True)
            raise HTTPException(status_code=500, detail="Error deleting directory route")
