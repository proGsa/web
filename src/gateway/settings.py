from __future__ import annotations
import os

class Settings:
    def __init__(self) -> None:
        self.USE_MIRROR: bool = os.getenv("USE_MIRROR", "false").lower() == "true"
        self.DB_MODE: str = os.getenv("DB_MODE", "write")  # write или read
        self.NODE_NAME: str = os.getenv("NODE_NAME", "app_main")

        self.DB_USER: str = os.getenv("DB_USER", "write_user")
        self.DB_PASSWORD: str = os.getenv("DB_PASSWORD", "write_password")
        self.DB_NAME: str = os.getenv("DB_NAME", "mydb")
        self.DB_PORT: str = os.getenv("DB_PORT", "5432")
        
        self.DB_MASTER_HOST: str = os.getenv("DB_HOST", "db-master")
        self.DB_SLAVE_HOST: str = os.getenv("DB_SLAVE_HOST", "db-slave")

        if self.USE_MIRROR and self.DB_MODE == "read":
            self.DATABASE_URL_ASYNC = (
                f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_SLAVE_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            )
        else:
            self.DATABASE_URL_ASYNC = (
                f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_MASTER_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            )
        self.CORE_SERVICE_URL: str = os.getenv("CORE_SERVICE_URL", "http://core:8000")
        self.ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
        
        self.RABBIT_URL: str = os.getenv(
            "RABBIT_URL", "amqp://user:pass@rabbitmq:5672/"
        )
        self.RABBIT_QUEUES: list[str] = os.getenv(
            "RABBIT_QUEUES",
            "TRAVEL_CREATED,USER_CREATED,ENTERTAINMENT_CREATED,ACCOMMODATION_CREATED"
        ).split(",")
settings = Settings()