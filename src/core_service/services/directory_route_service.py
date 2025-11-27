from __future__ import annotations

import logging

from ..abstract_repository.idirectory_route_repository import IDirectoryRouteRepository
from ..abstract_service.directory_route_service import IDirectoryRouteService
from ..shared.models.directory_route import DirectoryRoute

logger = logging.getLogger(__name__)


# class DirectoryRouteService(IDirectoryRouteService):
#     def __init__(self, repository: IDirectoryRouteRepository, publisher) -> None:
#         self.repository = repository
#         self.publisher = publisher
#         logger.debug("DirectoryRouteService инициализирован")

#     async def get_by_id(self, d_route_id: int) -> DirectoryRoute | None:
#         logger.debug("Получение справочника маршрутов по ID %d", d_route_id)
#         return await self.repository.get_by_id(d_route_id)

#     async def get_list(self) -> list[DirectoryRoute]:
#         logger.debug("Получение списка всех справочников маршрутов")
#         return await self.repository.get_list()

#     async def add(self, d_route: DirectoryRoute) -> DirectoryRoute:
#         try:
#             logger.debug("Добавление справочника маршрутов с ID %d", d_route.d_route_id)
#             d_route = await self.repository.add(d_route)
#             await self.publisher.publish(
#                 D_ROUTE_CREATED,
#                 d_route.model_dump(),
#             )
#         except (Exception):
#             logger.error("Справочник маршрутов c таким ID %d уже существует.", d_route.d_route_id)
#             raise ValueError("Cпpaвoчник маршрутов c таким ID уже существует.")
#         return d_route

#     async def update(self, updated_d_route: DirectoryRoute) -> DirectoryRoute:
#         try:
#             logger.debug("Обновление справочника маршрутов с ID %d", updated_d_route.d_route_id)
#             await self.repository.update(updated_d_route)
#             await self.publisher.publish(
#                 D_ROUTE_UPDATED,
#                 updated_d_route.model_dump(),
#             )
#         except (Exception):
#             logger.error("Справочник маршрутов с ID %d не найден.", updated_d_route.d_route_id)
#             raise ValueError("Cпpaвoчник маршрутов не найден.")
#         return updated_d_route

#     async def delete(self, d_route_id: int) -> None:
#         try:
#             logger.debug("Удаление справочника маршрутов с ID %d", d_route_id)
#             await self.repository.delete(d_route_id)
#             await self.publisher.publish(
#                 D_ROUTE_DELETED,
#                 {"id": d_route_id},
#             )
#         except (Exception):
#             logger.error("Не удалось удалить справочник маршрутов с ID %d", d_route_id)
#             raise ValueError("Cпpaвoчник маршрутов не получилось удалить.")

#     async def change_transport(self, d_route_id: int, new_transport: str) -> DirectoryRoute | None:
#         try:
#             logger.debug("Изменение транспорта в справочнике маршрутов %d на %s", 
#                         d_route_id, new_transport)
#             d_route = await self.repository.change_transport(d_route_id, new_transport)

#             await self.publisher.publish(
#                 D_ROUTE_UPDATED,
#                 d_route.model_dump(),
#             )

#             return d_route
#         except (Exception):
#             logger.error("Не удалось изменить транспорт в справочнике маршрутов %d", d_route_id)
#             raise ValueError("Не получилось изменить транспорт.")

#     async def get_by_cities(self, from_city_id: int, to_city_id: int, transport: str) -> DirectoryRoute | None:
#         try:
#             logger.debug("Удалось найти справочник маршрутов по городам %s и %s", from_city_id, to_city_id)
#             return await self.repository.get_by_cities(from_city_id, to_city_id, transport)
#         except (Exception):
#             logger.error("Не удалось найти справочник маршрутов по городам %s и %s", from_city_id, to_city_id)
#             raise ValueError("Cпpaвoчник маршрутов не получилось удалить.")

class DirectoryRouteService(IDirectoryRouteService):
    def __init__(self, rpc_client) -> None:
        self.rpc = rpc_client
        logger.debug("DirectoryRouteService инициализирован")

    # ----------------------------------------------
    # GET BY ID
    # ----------------------------------------------
    async def get_by_id(self, d_route_id: int) -> DirectoryRoute | None:
        logger.debug("RPC: directory_route.get_by_id %d", d_route_id)

        response = await self.rpc.call(
            "directory_route.get_by_id",
            {"id": d_route_id}
        )

        return DirectoryRoute(**response) if response else None

    # ----------------------------------------------
    # GET LIST
    # ----------------------------------------------
    async def get_list(self) -> list[DirectoryRoute]:
        logger.debug("RPC: directory_route.get_list")

        items = await self.rpc.call(
            "directory_route.get_list",
            {}
        )

        return [DirectoryRoute(**item) for item in items]

    # ----------------------------------------------
    # ADD
    # ----------------------------------------------
    async def add(self, d_route: DirectoryRoute) -> DirectoryRoute:
        logger.debug("RPC: directory_route.add %s", d_route)

        response = await self.rpc.call(
            "directory_route.add",
            d_route.model_dump()
        )

        return DirectoryRoute(**response)

    # ----------------------------------------------
    # UPDATE
    # ----------------------------------------------
    async def update(self, updated_d_route: DirectoryRoute) -> DirectoryRoute:
        logger.debug("RPC: directory_route.update %s", updated_d_route)

        response = await self.rpc.call(
            "directory_route.update",
            updated_d_route.model_dump()
        )
        return DirectoryRoute(**response)

    # ----------------------------------------------
    # DELETE
    # ----------------------------------------------
    async def delete(self, d_route_id: int) -> None:
        logger.debug("RPC: directory_route.delete %d", d_route_id)

        await self.rpc.call(
            "directory_route.delete",
            {"id": d_route_id}
        )

    # ----------------------------------------------
    # CHANGE TRANSPORT
    # ----------------------------------------------
    async def change_transport(self, d_route_id: int, new_transport: str) -> DirectoryRoute | None:
        logger.debug(
            "RPC: directory_route.change_transport %d -> %s",
            d_route_id, new_transport
        )

        response = await self.rpc.call(
            "directory_route.change_transport",
            {"id": d_route_id, "transport": new_transport}
        )
        return DirectoryRoute(**response) if response else None

    # ----------------------------------------------
    # GET BY CITIES
    # ----------------------------------------------
    async def get_by_cities(self, from_city_id: int, to_city_id: int, transport: str) -> DirectoryRoute | None:
        logger.debug(
            "RPC: directory_route.get_by_cities from=%d to=%d transport=%s",
            from_city_id, to_city_id, transport
        )

        response = await self.rpc.call(
            "directory_route.get_by_cities",
            {
                "from_city_id": from_city_id,
                "to_city_id": to_city_id,
                "transport": transport,
            }
        )

        return DirectoryRoute(**response) if response else None