from __future__ import annotations

import logging
from dataclasses import dataclass

from .messaging.rpc_client import CoreRPCClient, CoreRPCServer

from .services.accommodation_service import AccommodationService
from .services.city_service import CityService
from .services.directory_route_service import DirectoryRouteService
from .services.entertainment_service import EntertainmentService
from .services.route_service import RouteService
from .services.travel_service import TravelService
from .services.user_service import UserService, AuthService

# Контроллеры V1
from .controllers.api_v1.accommodation_controller import AccommodationController as AccommodationControllerV1
from .controllers.api_v1.city_controller import CityController as CityControllerV1
from .controllers.api_v1.d_route_controller import DirectoryRouteController as DirectoryRouteControllerV1
from .controllers.api_v1.entertainment_controller import EntertainmentController as EntertainmentControllerV1
from .controllers.api_v1.route_controller import RouteController as RouteControllerV1
from .controllers.api_v1.travel_controller import TravelController as TravelControllerV1
from .controllers.api_v1.user_controller import UserController as UserControllerV1

# Контроллеры V2
from .controllers.api_v2.accommodation_controller import AccommodationController as AccommodationControllerV2
from .controllers.api_v2.city_controller import CityController as CityControllerV2
from .controllers.api_v2.d_route_controller import DirectoryRouteController as DirectoryRouteControllerV2
from .controllers.api_v2.entertainment_controller import EntertainmentController as EntertainmentControllerV2
from .controllers.api_v2.route_controller import RouteController as RouteControllerV2
from .controllers.api_v2.travel_controller import TravelController as TravelControllerV2
from .controllers.api_v2.user_controller import UserController as UserControllerV2

logger = logging.getLogger(__name__)


class Services:
    def __init__(
        self,
        acc_serv: AccommodationService,
        city_serv: CityService,
        d_route_serv: DirectoryRouteService,
        ent_serv: EntertainmentService,
        route_serv: RouteService,
        travel_serv: TravelService,
        user_serv: UserService,
        auth_serv: AuthService,
    ):
        self.acc_serv = acc_serv
        self.city_serv = city_serv
        self.d_route_serv = d_route_serv
        self.ent_serv = ent_serv
        self.route_serv = route_serv
        self.travel_serv = travel_serv
        self.user_serv = user_serv
        self.auth_serv = auth_serv


@dataclass
class ControllersV1:
    acc_contr: AccommodationControllerV1
    city_contr: CityControllerV1
    route_contr: RouteControllerV1
    d_route_contr: DirectoryRouteControllerV1
    ent_contr: EntertainmentControllerV1
    travel_contr: TravelControllerV1
    user_contr: UserControllerV1


@dataclass
class ControllersV2:
    acc_contr: AccommodationControllerV2
    city_contr: CityControllerV2
    route_contr: RouteControllerV2
    d_route_contr: DirectoryRouteControllerV2
    ent_contr: EntertainmentControllerV2
    travel_contr: TravelControllerV2
    user_contr: UserControllerV2


class CoreServiceLocator:
    def __init__(self, services: Services, controllers_v1: ControllersV1, controllers_v2: ControllersV2):
        self.services = services
        self.controllers_v1 = controllers_v1
        self.controllers_v2 = controllers_v2

    # Services
    def get_acc_serv(self) -> AccommodationService:
        return self.services.acc_serv

    def get_city_serv(self) -> CityService:
        return self.services.city_serv

    def get_d_route_serv(self) -> DirectoryRouteService:
        return self.services.d_route_serv

    def get_ent_serv(self) -> EntertainmentService:
        return self.services.ent_serv

    def get_route_serv(self) -> RouteService:
        return self.services.route_serv

    def get_travel_serv(self) -> TravelService:
        return self.services.travel_serv

    def get_user_serv(self) -> UserService:
        return self.services.user_serv

    def get_auth_serv(self) -> AuthService:
        return self.services.auth_serv

    # Controllers
    def get_controllers_v1(self) -> ControllersV1:
        return self.controllers_v1

    def get_controllers_v2(self) -> ControllersV2:
        return self.controllers_v2


# ---------------------------------------------------------
#              FULL get_service_locator
# ---------------------------------------------------------
async def get_service_locator() -> CoreServiceLocator:
    logger.info("Core Service: инициализация зависимостей...")

    # RPC Client
    rpc_client = CoreRPCClient("amqp://user:pass@rabbitmq:5672/")
    await rpc_client.connect()

    # Services
    acc_serv = AccommodationService(rpc_client)
    city_serv = CityService(rpc_client)
    d_route_serv = DirectoryRouteService(rpc_client)
    ent_serv = EntertainmentService(rpc_client)
    route_serv = RouteService(rpc_client)
    travel_serv = TravelService(rpc_client)
    user_serv = UserService(rpc_client)
    auth_serv = AuthService(rpc_client)

    services = Services(
        acc_serv, city_serv, d_route_serv, ent_serv,
        route_serv, travel_serv, user_serv, auth_serv
    )
    rpc_server = CoreRPCServer(
        city_service=city_serv,
        user_service=user_serv,
        acc_service=acc_serv,
        d_route_service=d_route_serv,
        ent_service=ent_serv,
        route_service=route_serv,
        travel_service=travel_serv,
        auth_service=auth_serv
    )
    await rpc_server.connect()

    # Controllers V1
    controllers_v1 = ControllersV1(
        acc_contr=AccommodationControllerV1(acc_serv, city_serv),
        city_contr=CityControllerV1(city_serv),
        route_contr=RouteControllerV1(route_serv, travel_serv, d_route_serv, user_serv, ent_serv, acc_serv),
        d_route_contr=DirectoryRouteControllerV1(d_route_serv, city_serv),
        ent_contr=EntertainmentControllerV1(ent_serv, city_serv),
        travel_contr=TravelControllerV1(travel_serv, user_serv, ent_serv, acc_serv),
        user_contr=UserControllerV1(user_serv, auth_serv)
    )

    # Controllers V2
    controllers_v2 = ControllersV2(
        acc_contr=AccommodationControllerV2(acc_serv, city_serv),
        city_contr=CityControllerV2(city_serv),
        route_contr=RouteControllerV2(route_serv, travel_serv, d_route_serv, user_serv, ent_serv, acc_serv),
        d_route_contr=DirectoryRouteControllerV2(d_route_serv, city_serv),
        ent_contr=EntertainmentControllerV2(ent_serv, city_serv),
        travel_contr=TravelControllerV2(travel_serv, user_serv, ent_serv, acc_serv, city_serv),
        user_contr=UserControllerV2(user_serv, auth_serv)
    )

    logger.info("Core Service: зависимости успешно инициализированы")
    return CoreServiceLocator(services, controllers_v1, controllers_v2)
