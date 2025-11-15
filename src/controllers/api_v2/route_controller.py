from __future__ import annotations

import logging

from models.route import Route
from schemas.route import InsertCityRequest
from schemas.route import RouteCreate
from schemas.route import RouteResponse
from schemas.route import RouteUpdate
from services.accommodation_service import AccommodationService
from services.directory_route_service import DirectoryRouteService
from services.entertainment_service import EntertainmentService
from services.route_service import RouteService
from services.travel_service import TravelService
from services.user_service import UserService


logger = logging.getLogger(__name__)


class RouteController:
    def __init__(self, route_service: RouteService, travel_service: TravelService,
        d_route_service: DirectoryRouteService, user_service: UserService,
        ent_service: EntertainmentService, acc_service: AccommodationService) -> None:
        self.route_service = route_service
        self.travel_service = travel_service
        self.d_route_service = d_route_service
        self.user_service = user_service
        self.ent_service = ent_service
        self.acc_service = acc_service
        logger.debug("RouteController initialized")

    async def create_route(self, route_data: RouteCreate) -> RouteResponse:
        """Создать новый маршрут"""
        try:
            d_route = await self.d_route_service.get_by_id(route_data.d_route_id)
            if not d_route:
                logger.warning(f"Directory route ID {route_data.d_route_id} не найден")
                return None

            travel = await self.travel_service.get_by_id(route_data.travel_id)
            if not travel:
                logger.warning(f"Travel ID {route_data.travel_id} не найден")
                return None

            route = Route(
                route_id=1,
                d_route=d_route,
                travels=travel,
                start_time=route_data.start_time.replace(tzinfo=None),
                end_time=route_data.end_time.replace(tzinfo=None),
                type=route_data.type
            )

            route = await self.route_service.add(route)
            logger.info(f"Маршрут ID {route.route_id} создан")

            return RouteResponse(
                route_id=route.route_id,
                d_route_id=d_route.d_route_id,
                travel_id=travel.travel_id,
                start_time=route.start_time,
                end_time=route.end_time,
                type=route.type
            )
        except Exception as e:
            logger.error(f"Ошибка при создании маршрута: {e!s}", exc_info=True)
            raise

    async def get_route_by_id(self, route_id: int) -> RouteResponse | None:
        """Получить маршрут по ID"""
        try:
            route = await self.route_service.get_by_id(route_id)
            if not route or not route.d_route or not route.travels:
                logger.warning(f"Маршрут ID {route_id} не найден")
                return None

            return RouteResponse(
                route_id=route.route_id,
                d_route_id=route.d_route.d_route_id,
                travel_id=route.travels.travel_id,
                start_time=route.start_time,
                end_time=route.end_time,
                type=route.type
            )
        except Exception as e:
            logger.error(f"Ошибка при получении маршрута ID {route_id}: {e!s}", exc_info=True)
            raise

    async def get_all_routes(self) -> list[RouteResponse]:
        try:
            route_list = await self.route_service.get_all_routes()
            responses = []
            for r in route_list:
                if r and r.d_route and r.travels:
                    responses.append(RouteResponse(
                        route_id=r.route_id,
                        d_route_id=r.d_route.d_route_id,
                        travel_id=r.travels.travel_id,
                        start_time=r.start_time,
                        end_time=r.end_time,
                        type=r.type
                    ))
            logger.info(f"Получено {len(responses)} маршрутов")
            return responses
        except Exception as e:
            logger.error(f"Ошибка при получении всех маршрутов: {e!s}", exc_info=True)
            raise

    async def update_route(self, route_id: int, route_data: RouteUpdate) -> RouteResponse | None:
        try:
            existing_route = await self.route_service.get_by_id(route_id)
            if not existing_route:
                logger.warning(f"Маршрут ID {route_id} не найден для обновления")
                return None
            d_route = await self.d_route_service.get_by_id(route_data.d_route_id)
            if not d_route:
                logger.warning(f"Directory route ID {route_data.d_route_id} не найден")
                return None

            travel = await self.travel_service.get_by_id(route_data.travel_id)
            if not travel:
                logger.warning(f"Travel ID {route_data.travel_id} не найден")
                return None
                
            route = Route(
                route_id=route_id,
                d_route=d_route,
                travels=travel,
                start_time=route_data.start_time.replace(tzinfo=None),
                end_time=route_data.end_time.replace(tzinfo=None),
                type=route_data.type
            )

            updated_route = await self.route_service.update(route)
            logger.info(f"Маршрут ID {route_id} обновлён")
            return RouteResponse(
                route_id=updated_route.route_id,
                d_route_id=updated_route.d_route.d_route_id,
                travel_id=updated_route.travels.travel_id,
                start_time=updated_route.start_time,
                end_time=updated_route.end_time,
                type=updated_route.type
            )
        except Exception as e:
            logger.error(f"Ошибка при обновлении маршрута ID {route_id}: {e!s}", exc_info=True)
            raise

    async def delete_route(self, route_id: int) -> None:
        try:
            await self.route_service.delete(route_id)
            logger.info(f"Маршрут ID {route_id} успешно удалён")
        except Exception as e:
            logger.error(f"Ошибка при удалении маршрута ID {route_id}: {e!s}", exc_info=True)
            raise

    async def insert_city_after(self, travel_id: int, new_city_id: int, request: InsertCityRequest) -> None:
        try:
            logger.debug(
                "Вставка города %d после города %d в путешествии %d с транспортом %s",
                new_city_id, request.after_city_id, travel_id, request.transport
            )
            await self.route_service.insert_city_after(travel_id, new_city_id, request.after_city_id, request.transport)
        except ValueError as e:
            logger.error("Ошибка вставки города: %s", e)
            raise
        except Exception as e:
            logger.error("Внутренняя ошибка при вставке города: %s", e, exc_info=True)
            raise

    async def delete_city_from_route(self, travel_id: int, city_id: int) -> None:
        try:
            logger.debug("Удаление города %d из маршрута %d", city_id, travel_id)
            await self.route_service.delete_city_from_route(travel_id, city_id)
        except ValueError as e:
            logger.error("Ошибка удаления города: %s", e)
            raise
        except Exception as e:
            logger.error("Внутренняя ошибка при удалении города: %s", e, exc_info=True)
            raise