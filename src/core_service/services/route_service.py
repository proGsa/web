from __future__ import annotations

import logging

from typing import Any

from ..abstract_repository.iroute_repository import IRouteRepository
from ..abstract_service.route_service import IRouteService
from ..shared.models.route import Route


logger = logging.getLogger(__name__)

Route.model_rebuild()


# class RouteService(IRouteService):
#     def __init__(self, repository: IRouteRepository, publisher) -> None:
#         self.repository = repository
#         self.publisher = publisher
#         logger.debug("RouteService инициализирован")

#     async def get_by_id(self, route_id: int) -> Route | None:
#         logger.debug("Получение маршрута по ID %d", route_id)
#         return await self.repository.get_by_id(route_id)

#     async def get_all_routes(self) -> list[Route]:
#         logger.debug("Получение списка всех маршрутов")
#         return await self.repository.get_list()

#     async def add(self, route: Route) -> Route:
#         try:
#             logger.debug("Добавление маршрута с ID %d", route.route_id)
#             route = await self.repository.add(route)
#             await self.publisher.publish(
#                 ROUTE_CREATED,
#                 route.model_dump(),
#             )
#         except (Exception):
#             logger.error("Маршрут c таким ID %d уже существует.", route.route_id)
#             raise ValueError("Маршрут c таким ID уже существует.")
#         return route

#     async def update(self, updated_route: Route) -> Route:
#         try:
#             logger.debug("Обновление маршрута с ID %d", updated_route.route_id)
#             await self.repository.update(updated_route)
#             await self.publisher.publish(
#                 ROUTE_UPDATED,
#                 updated_route.model_dump(),
#             )
#         except (Exception):
#             logger.error("Маршрут с ID %d не найден.", updated_route.route_id)
#             raise ValueError("Маршрут не найден.")
#         return updated_route

#     async def delete(self, route_id: int) -> None:
#         try:
#             logger.debug("Удаление маршрута с ID %d", route_id)
#             await self.repository.delete(route_id)
#             await self.publisher.publish(
#                 ROUTE_DELETED,
#                 {"id": route_id},
#             )
#         except (Exception):
#             logger.error("Маршрут с ID %d не найден.", route_id)
#             raise ValueError("Маршрут не найден.")

#     async def insert_city_after(self, travel_id: int, new_city_id: int, after_city_id: int, transport: str) -> None:
#         try:
#             logger.debug("Добавление %d города после города %d в путешествии %d", 
#                         new_city_id, after_city_id, travel_id)
#             await self.repository.insert_city_after(travel_id, new_city_id, after_city_id, transport)
#             await self.publisher.publish(
#                 ROUTE_UPDATED, 
#                 {"travel_id": travel_id, "new_city_id": new_city_id, "after_city_id": after_city_id}
#             )

#         except (Exception):
#             logger.error("Не удалось добавить город %d в маршрут", new_city_id)
#             raise ValueError("Город не получилось добавить.")

#     async def delete_city_from_route(self, travel_id: int, city_id: int) -> None:
#         try:
#             logger.debug("Удаление города %d из маршрута", city_id)
#             await self.repository.delete_city_from_route(travel_id, city_id)
#             await self.publisher.publish(
#                 ROUTE_UPDATED,
#                 {"travel_id": travel_id, "deleted_city_id": city_id}
#             )
#         except (Exception):
#             logger.error("Не удалось удалить город %d из маршрута", city_id)
#             raise ValueError("Город не получилось удалить из маршрута.")

#     async def change_transport(self, d_route_id: int, route_id: int, new_transport: str) -> Route | None:
#         try:
#             logger.debug("Изменение транспорта в маршруте %d на %s", 
#                         route_id, new_transport)
#             route = await self.repository.change_transport(d_route_id, route_id, new_transport)
#             await self.publisher.publish(
#                 ROUTE_UPDATED,
#                 route.model_dump(),
#             )
#             return route
#         except (Exception):
#             logger.error("Не удалось изменить транспорт в маршруте %d", route_id)
#             raise ValueError("Город не получилось удалить из маршрута.")

#     async def get_routes_by_user_and_status_and_type(self, user_id: int, status: str, type_route: str) -> list[Route]:
#         logger.debug("Получение маршрута по user_id %d, status %s, type: %s", user_id, status, type_route)
#         return await self.repository.get_routes_by_user_and_status_and_type(user_id, status, type_route)

#     async def get_routes_by_type(self, type_route: str) -> list[Route]:
#         logger.debug("Получение маршрута по type: %s", type_route)
#         return await self.repository.get_routes_by_type(type_route)

#     async def get_route_parts(self, route_id: int) -> list[dict[str, Any]]:
        # return await self.repository.get_route_parts(route_id)


class RouteService(IRouteService):
    def __init__(self, rpc_client) -> None:
        self.rpc = rpc_client
        logger.debug("RouteService инициализирован")

    async def get_by_id(self, route_id: int) -> Route | None:
        logger.debug("RPC: route.get_by_id %d", route_id)
        response = await self.rpc.call("route.get_by_id", {"id": route_id})
        return Route(**response) if response else None

    async def get_all_routes(self) -> list[Route]:
        logger.debug("RPC: route.get_all_routes")
        items = await self.rpc.call("route.get_all_routes", {})
        return [Route(**item) for item in items]

    async def add(self, route: Route) -> Route:
        logger.debug("RPC: route.add %s", route)
        response = await self.rpc.call("route.add", route.model_dump())
        return Route(**response)

    async def update(self, updated_route: Route) -> Route:
        logger.debug("RPC: route.update %s", updated_route)
        response = await self.rpc.call("route.update", updated_route.model_dump())
        return Route(**response)

    async def delete(self, route_id: int) -> None:
        logger.debug("RPC: route.delete %d", route_id)
        await self.rpc.call("route.delete", {"id": route_id})

    async def insert_city_after(self, travel_id: int, new_city_id: int, after_city_id: int, transport: str) -> None:
        logger.debug(
            "RPC: route.insert_city_after: new_city %d after_city %d travel %d", 
            new_city_id, after_city_id, travel_id
        )
        await self.rpc.call(
            "route.insert_city_after",
            {
                "travel_id": travel_id,
                "new_city_id": new_city_id,
                "after_city_id": after_city_id,
                "transport": transport
            }
        )


    async def delete_city_from_route(self, travel_id: int, city_id: int) -> None:
        logger.debug("RPC: route.delete_city_from_route travel %d city %d", travel_id, city_id)
        await self.rpc.call("route.delete_city_from_route", {"travel_id": travel_id, "city_id": city_id})

    async def change_transport(self, d_route_id: int, route_id: int, new_transport: str) -> Route | None:
        logger.debug("RPC: route.change_transport route %d new_transport %s", route_id, new_transport)
        response = await self.rpc.call(
            "route.change_transport",
            {"d_route_id": d_route_id, "route_id": route_id, "new_transport": new_transport}
        )
        route = Route(**response) if response else None

        return route

    async def get_routes_by_user_and_status_and_type(self, user_id: int, status: str, type_route: str) -> list[Route]:
        logger.debug("RPC: route.get_routes_by_user_and_status_and_type user %d status %s type %s", user_id, status, type_route)
        items = await self.rpc.call(
            "route.get_routes_by_user_and_status_and_type",
            {"user_id": user_id, "status": status, "type": type_route}
        )
        return [Route(**item) for item in items]

    async def get_routes_by_type(self, type_route: str) -> list[Route]:
        logger.debug("RPC: route.get_routes_by_type type %s", type_route)
        items = await self.rpc.call("route.get_routes_by_type", {"type": type_route})
        return [Route(**item) for item in items]

    async def get_route_parts(self, route_id: int) -> list[dict[str, Any]]:
        logger.debug("RPC: route.get_route_parts %d", route_id)
        return await self.rpc.call("route.get_route_parts", {"route_id": route_id})