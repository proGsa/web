# gateway_service/service_locator.py
from dataclasses import dataclass
from .messaging.messaging_service import MessagingService
from .shared.schemas.directory_route import DirectoryRouteCreate, DirectoryRouteUpdate, DirectoryRoutePartialUpdate
from .shared.schemas.entertainment import EntertainmentCreate, EntertainmentUpdate
from typing import List, Optional, Any
from .shared.schemas.route import RouteCreate, RouteUpdate, InsertCityRequest
from .shared.schemas.travel import TravelCreate, TravelUpdate
from .shared.schemas.travel import TravelCreate, TravelUpdate
from .shared.schemas.entertainment import EntertainmentCreate
from .shared.schemas.accommodation import AccommodationCreate, AccommodationResponse
from .messaging.messaging_service import MessagingService
from .shared.schemas.auth import LoginRequest, LoginResponse
from .shared.schemas.city import CityResponse
from .shared.schemas.user import UserCreate, UserUpdate, UserResponse, UsersResponse

class UserControllerGatewayV1:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    # --- User CRUD ---
    async def create_new_user(self, user: UserCreate) -> Any:
        return await self.messaging.rpc_call("core_user_create", user.dict())

    async def update_user(self, user_id: int, user: UserUpdate) -> Any:
        payload = {"user_id": user_id, **user.dict()}
        return await self.messaging.rpc_call("core_user_update", payload)

    async def delete_user(self, user_id: int) -> Any:
        return await self.messaging.rpc_call("core_user_delete", {"user_id": user_id})

    async def get_user_profile(self, user_id: int) -> Any:
        return await self.messaging.rpc_call("core_user_get_profile", {"user_id": user_id})

    async def get_all_users(self) -> List[Any]:
        return await self.messaging.rpc_call("core_user_get_all", {})

    # --- Auth ---
    async def registrate(self, user: UserCreate) -> dict[str, Any]:
        return await self.messaging.rpc_call("core_user_register", user.dict())

    async def login(self, email: str, password: str) -> dict[str, Any]:
        payload = {"email": email, "password": password}
        return await self.messaging.rpc_call("core_user_login", payload)

class CityControllerGatewayV1:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    async def create_new_city(self, data):
        return await self.messaging.rpc_call("core_city_create", data)

    async def get_all_cities(self):
        return await self.messaging.rpc_call("core_city_get_all", {})

    async def get_city_details(self, city_id: int):
        return await self.messaging.rpc_call("core_city_get", {"city_id": city_id})

    async def update_city(self, city_id: int, data):
        return await self.messaging.rpc_call("core_city_update", {"city_id": city_id, **data.dict()})

    async def delete_city(self, city_id: int):
        return await self.messaging.rpc_call("core_city_delete", {"city_id": city_id})

class AccommodationControllerGatewayV1:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    async def create_new_accommodation(self, data):
        payload = data.dict() if hasattr(data, "dict") else data
        for field in ("check_in", "check_out"):
            if field in payload and hasattr(payload[field], "isoformat"):
                payload[field] = payload[field].isoformat()

        acc =  await self.messaging.rpc_call("core_accommodation_create", payload)
        accommodation = AccommodationResponse(accommodation_id=acc["accommodation_id"], name=acc["name"], city_id=acc["city"]["city_id"],
                        address=acc["address"], price=acc["price"], type=acc["type"], 
                        rating=acc["rating"], check_in=acc["check_in"], check_out=acc["check_out"])
        return accommodation

    async def get_all_accommodations(self):
        response = await self.messaging.rpc_call("core_accommodation_get_all", {})

        accommodations = [
            AccommodationResponse(accommodation_id=acc["accommodation_id"], name=acc["name"], city_id=acc["city"]["city_id"],
                        address=acc["address"], price=acc["price"], type=acc["type"], 
                        rating=acc["rating"], check_in=acc["check_in"], check_out=acc["check_out"])
            for acc in response
        ]
        return accommodations

    async def get_accommodation_details(self, accommodation_id: int):
        acc = await self.messaging.rpc_call("core_accommodation_get", {"accommodation_id": accommodation_id})
        accommodation = AccommodationResponse(accommodation_id=acc["accommodation_id"], name=acc["name"], city_id=acc["city"]["city_id"],
                        address=acc["address"], price=acc["price"], type=acc["type"], 
                        rating=acc["rating"], check_in=acc["check_in"], check_out=acc["check_out"])
        return accommodation


    async def update_accommodation(self, accommodation_id: int, data):
        payload = {"accommodation_id": accommodation_id}
        if hasattr(data, "dict"):
            payload.update(data.dict())
        else:
            payload.update(data)
        response = await self.messaging.rpc_call("core_accommodation_update", payload)
        accommodation = AccommodationResponse(accommodation_id=acc["accommodation_id"], name=acc["name"], city_id=acc["city"]["city_id"],
                        address=acc["address"], price=acc["price"], type=acc["type"], 
                        rating=acc["rating"], check_in=acc["check_in"], check_out=acc["check_out"])
        return accommodation

    async def delete_accommodation(self, accommodation_id: int):
        return await self.messaging.rpc_call("core_accommodation_delete", {"accommodation_id": accommodation_id})

    async def link_accommodation_to_route(self, travel_id: int, accommodation_ids: list[int]):
        return await self.messaging.rpc_call(
            "core_travel_link_accommodations",
            {"travel_id": travel_id, "accommodation_ids": accommodation_ids}
        )

    async def delete_accommodation_from_route(self, accommodation_id: int):
        return await self.messaging.rpc_call(
            "core_travel_delete_accommodation",
            {"accommodation_id": accommodation_id}
        )

class DirectoryRouteControllerGatewayV1:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    async def create_new_d_route(self, data: DirectoryRouteCreate):
        return await self.messaging.rpc_call("core_d_route_create", data.dict())

    async def get_all_d_routes(self):
        return await self.messaging.rpc_call("core_d_route_get_all", {})

    async def get_d_route_details(self, d_route_id: int):
        return await self.messaging.rpc_call("core_d_route_get", {"d_route_id": d_route_id})

    async def update_d_route(self, d_route_id: int, data: DirectoryRouteUpdate):
        return await self.messaging.rpc_call(
            "core_d_route_update", {"d_route_id": d_route_id, **data.dict()}
        )

    async def delete_d_route(self, d_route_id: int):
        return await self.messaging.rpc_call("core_d_route_delete", {"d_route_id": d_route_id})

class EntertainmentControllerGatewayV1:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    async def create_new_entertainment(self, data: EntertainmentCreate):
        return await self.messaging.rpc_call("core_entertainment_create", data.dict())

    async def get_all_entertainment(self):
        return await self.messaging.rpc_call("core_entertainment_get_all", {})

    async def get_entertainment_details(self, entertainment_id: int):
        return await self.messaging.rpc_call("core_entertainment_get", {"entertainment_id": entertainment_id})

    async def update_entertainment(self, entertainment_id: int, data: EntertainmentUpdate):
        return await self.messaging.rpc_call(
            "core_entertainment_update", {"entertainment_id": entertainment_id, **data.dict()}
        )

    async def delete_entertainment(self, entertainment_id: int):
        return await self.messaging.rpc_call("core_entertainment_delete", {"entertainment_id": entertainment_id})

    async def update_entertainment_dates(self, entertainment_id: int, data: EntertainmentUpdate):
        return await self.messaging.rpc_call(
            "core_entertainment_update_dates", {"entertainment_id": entertainment_id, **data.dict()}
        )

class RouteControllerGatewayV1:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    async def create_new_route(self, route_data: RouteCreate):
        return await self.messaging.rpc_call("core_route_create", route_data.dict())

    async def get_all_routes(self) -> List:
        return await self.messaging.rpc_call("core_route_get_all", {})

    async def get_route_by_id(self, route_id: int):
        return await self.messaging.rpc_call("core_route_get", {"route_id": route_id})

    async def update_route(self, route_id: int, route_data: RouteUpdate):
        return await self.messaging.rpc_call(
            "core_route_update", {"route_id": route_id, **route_data.dict()}
        )

    async def delete_route(self, route_id: int):
        return await self.messaging.rpc_call("core_route_delete", {"route_id": route_id})

    async def get_route_parts(self, route_id: int) -> List:
        return await self.messaging.rpc_call("core_route_get_parts", {"route_id": route_id})

    async def change_transport(self, route_id: int, transport: str):
        return await self.messaging.rpc_call(
            "core_route_change_transport", {"route_id": route_id, "transport": transport}
        )

    async def delete_city_from_route(self, route_id: int, city_id: int):
        return await self.messaging.rpc_call(
            "core_route_delete_city", {"route_id": route_id, "city_id": city_id}
        )

    async def add_new_city(self, route_id: int, city_id: int):
        return await self.messaging.rpc_call(
            "core_route_add_city", {"route_id": route_id, "city_id": city_id}
        )

    async def extend_travel_duration(self, route_id: int, extra_days: int):
        return await self.messaging.rpc_call(
            "core_route_extend_duration", {"route_id": route_id, "extra_days": extra_days}
        )

class TravelControllerGatewayV1:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    async def create_new_travel(self, travel_data: TravelCreate) -> Any:
        return await self.messaging.rpc_call("core_travel_create", travel_data.dict())

    async def get_all_travels(self) -> List[Any]:
        return await self.messaging.rpc_call("core_travel_get_all", {})

    async def get_travel_details(self, travel_id: int) -> Any:
        return await self.messaging.rpc_call("core_travel_get", {"travel_id": travel_id})

    async def update_travel(self, travel_id: int, travel_data: TravelUpdate) -> Any:
        return await self.messaging.rpc_call(
            "core_travel_update", {"travel_id": travel_id, **travel_data.dict()}
        )

    async def delete_travel(self, travel_id: int) -> None:
        await self.messaging.rpc_call("core_travel_delete", {"travel_id": travel_id})

    async def complete_travel(self, travel_id: int) -> Any:
        return await self.messaging.rpc_call("core_travel_complete", {"travel_id": travel_id})

@dataclass
class ControllersV1:
    acc_contr: AccommodationControllerGatewayV1
    city_contr: CityControllerGatewayV1
    route_contr: RouteControllerGatewayV1
    d_route_contr: DirectoryRouteControllerGatewayV1
    ent_contr: EntertainmentControllerGatewayV1
    travel_contr: TravelControllerGatewayV1
    user_contr: UserControllerGatewayV1


class ServiceLocatorV1:
    def __init__(self, controllers: ControllersV1, messaging: MessagingService):
        self.controllers = controllers
        self.messaging = messaging

    def get_acc_contr(self):
        return self.controllers.acc_contr
        
    def get_city_contr(self):
        return self.controllers.city_contr

    def get_d_route_contr(self):
        return self.controllers.d_route_contr
    
    def get_ent_contr(self):
        return self.controllers.ent_contr

    def get_route_contr(self):
        return self.controllers.route_contr

    def get_travel_contr(self):
        return self.controllers.travel_contr

    def get_user_contr(self):
        return self.controllers.user_contr

    def get_messaging(self):
        return self.messaging


async def get_service_locator_v1() -> ServiceLocatorV1:
    messaging = MessagingService()
    await messaging.connect()

    controllers = ControllersV1(
        acc_contr=AccommodationControllerGatewayV1(messaging),
        city_contr=CityControllerGatewayV1(messaging),
        route_contr=RouteControllerGatewayV1(messaging),
        d_route_contr=DirectoryRouteControllerGatewayV1(messaging),
        ent_contr=EntertainmentControllerGatewayV1(messaging),
        travel_contr=TravelControllerGatewayV1(messaging),
        user_contr=UserControllerGatewayV1(messaging)
    )

    return ServiceLocatorV1(controllers, messaging)


class CityControllerGatewayV2:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    async def create_city(self, data):
        payload = data.dict() if hasattr(data, "dict") else data
        response = await self.messaging.rpc_call("core_city_create", payload)
        
        return CityResponse(id=response["city_id"], name=response["name"])

    async def get_all_cities(self):
        response = await self.messaging.rpc_call("core_city_get_all", {})
        
        cities = [
            CityResponse(id=c["city_id"], name=c["name"])
            for c in response
        ]
        return cities

    async def get_city_by_id(self, city_id: int):
        response = await self.messaging.rpc_call("core_city_get", {"city_id": city_id})
        return CityResponse(id=response["city_id"], name=response["name"])

    async def update_city(self, city_id: int, data):
        payload = {"city_id": city_id}
        if hasattr(data, "dict"):
            payload.update(data.dict())
        else:
            payload.update(data)
        response = await self.messaging.rpc_call("core_city_update", payload)
        return CityResponse(id=response["city_id"], name=response["name"])

    async def delete_city(self, city_id: int):
        return await self.messaging.rpc_call("core_city_delete", {"city_id": city_id})

class AccommodationControllerGatewayV2(AccommodationControllerGatewayV1):
    pass

class DirectoryRouteControllerGatewayV2(DirectoryRouteControllerGatewayV1):
    async def partial_update_d_route(self, d_route_id: int, data: DirectoryRoutePartialUpdate):
        return await self.messaging.rpc_call(
            "core_d_route_partial_update", {"d_route_id": d_route_id, **data.dict(exclude_unset=True)}
        )

class EntertainmentControllerGatewayV2(EntertainmentControllerGatewayV1):
    pass

class TravelControllerGatewayV2:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    # --- Travels ---
    async def create_travel(self, travel: TravelCreate) -> Any:
        return await self.messaging.rpc_call("core_travel_create", travel.dict())

    async def get_all_travels(self) -> List[Any]:
        return await self.messaging.rpc_call("core_travel_get_all", {})

    async def get_travel_by_id(self, travel_id: int) -> Any:
        return await self.messaging.rpc_call("core_travel_get", {"travel_id": travel_id})

    async def update_travel(self, travel_id: int, travel: TravelUpdate) -> Any:
        return await self.messaging.rpc_call(
            "core_travel_update", {"travel_id": travel_id, **travel.dict()}
        )

    async def delete_travel(self, travel_id: int) -> None:
        await self.messaging.rpc_call("core_travel_delete", {"travel_id": travel_id})

    async def complete_travel(self, travel_id: int) -> Any:
        return await self.messaging.rpc_call("core_travel_complete", {"travel_id": travel_id})

    # --- Entertainments ---
    async def add_entertainment_to_travel(self, travel_id: int, entertainment: EntertainmentCreate) -> Any:
        payload = {"travel_id": travel_id, **entertainment.dict()}
        return await self.messaging.rpc_call("core_travel_add_entertainment", payload)

    async def delete_entertainment_from_travel(self, travel_id: int, entertainment_id: int) -> None:
        await self.messaging.rpc_call(
            "core_travel_delete_entertainment", {"travel_id": travel_id, "entertainment_id": entertainment_id}
        )

    # --- Accommodations ---
    async def add_accommodation_to_travel(self, travel_id: int, accommodation: AccommodationCreate) -> Any:
        payload = {"travel_id": travel_id, **accommodation.dict()}
        return await self.messaging.rpc_call("core_travel_add_accommodation", payload)

    async def delete_accommodation_from_travel(self, travel_id: int, accommodation_id: int) -> None:
        await self.messaging.rpc_call(
            "core_travel_delete_accommodation", {"travel_id": travel_id, "accommodation_id": accommodation_id}
        )

class RouteControllerGatewayV2:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    async def create_route(self, route: RouteCreate):
        return await self.messaging.rpc_call("core_route_create", route.dict())

    async def get_all_routes(self) -> List:
        return await self.messaging.rpc_call("core_route_get_all", {})

    async def get_route_by_id(self, route_id: int):
        return await self.messaging.rpc_call("core_route_get", {"route_id": route_id})

    async def update_route(self, route_id: int, route: RouteUpdate):
        return await self.messaging.rpc_call(
            "core_route_update", {"route_id": route_id, **route.dict()}
        )

    async def delete_route(self, route_id: int):
        return await self.messaging.rpc_call("core_route_delete", {"route_id": route_id})

    async def insert_city_after(self, travel_id: int, city_id: int, request: InsertCityRequest):
        return await self.messaging.rpc_call(
            "core_route_insert_city_after",
            {"travel_id": travel_id, "city_id": city_id, **request.dict()}
        )

    async def delete_city_from_route(self, travel_id: int, city_id: int):
        return await self.messaging.rpc_call(
            "core_route_delete_city", {"travel_id": travel_id, "city_id": city_id}
        )
class UserControllerGatewayV2:
    def __init__(self, messaging: MessagingService):
        self.messaging = messaging

    # --- Auth ---
    async def login(self, credentials: LoginRequest) -> LoginResponse:
        payload = credentials.dict()
        return await self.messaging.rpc_call("core_user_login", payload)

    # --- User CRUD ---
    async def create_user(self, user: UserCreate) -> UserResponse:
        return await self.messaging.rpc_call("core_user_create", user.dict())

    async def get_all_users(self) -> List[UserResponse]:
        return await self.messaging.rpc_call("core_user_get_all", {})

    async def get_user_profile(self, user_id: int) -> UserResponse:
        return await self.messaging.rpc_call("core_user_get_profile", {"user_id": user_id})

    async def update_user(self, user_id: int, user: UserUpdate) -> UserResponse:
        payload = {"user_id": user_id, **user.dict()}
        return await self.messaging.rpc_call("core_user_update", payload)

    async def delete_user(self, user_id: int) -> None:
        return await self.messaging.rpc_call("core_user_delete", {"user_id": user_id})
@dataclass
class ControllersV2:
    acc_contr: AccommodationControllerGatewayV2
    city_contr: CityControllerGatewayV2
    route_contr: RouteControllerGatewayV2
    d_route_contr: DirectoryRouteControllerGatewayV2
    ent_contr: EntertainmentControllerGatewayV2
    travel_contr: TravelControllerGatewayV2
    user_contr: UserControllerGatewayV2



class ServiceLocatorV2:
    def __init__(self, controllers: ControllersV2, messaging: MessagingService):
        self.controllers = controllers
        self.messaging = messaging

    def get_acc_contr(self):
        return self.controllers.acc_contr
        
    def get_city_contr(self):
        return self.controllers.city_contr

    def get_d_route_contr(self):
        return self.controllers.d_route_contr
    
    def get_ent_contr(self):
        return self.controllers.ent_contr

    def get_route_contr(self):
        return self.controllers.route_contr

    def get_travel_contr(self):
        return self.controllers.travel_contr

    def get_user_contr(self):
        return self.controllers.user_contr

    def get_messaging(self):
        return self.messaging

async def get_service_locator_v2() -> ServiceLocatorV2:
    messaging = MessagingService()
    await messaging.connect()

    controllers = ControllersV2(
        acc_contr=AccommodationControllerGatewayV2(messaging),
        city_contr=CityControllerGatewayV2(messaging),
        route_contr=RouteControllerGatewayV2(messaging),
        d_route_contr=DirectoryRouteControllerGatewayV2(messaging),
        ent_contr=EntertainmentControllerGatewayV2(messaging),
        travel_contr=TravelControllerGatewayV2(messaging),
        user_contr=UserControllerGatewayV2(messaging)
    )

    return ServiceLocatorV2(controllers, messaging)
