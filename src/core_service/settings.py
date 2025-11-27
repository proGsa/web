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

        self.RABBITMQ_HOST: str = os.getenv("RABBITMQ_HOST", "rabbitmq")
        self.RABBITMQ_PORT: int = int(os.getenv("RABBITMQ_PORT", 5672))
        self.RABBITMQ_USER: str = os.getenv("RABBITMQ_USER", "user")
        self.RABBITMQ_PASSWORD: str = os.getenv("RABBITMQ_PASSWORD", "password")

        self.SECRET_KEY: str = os.getenv("SECRET_KEY", "mysecret")
        self.ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
        self.SESSION_TIMEOUT: int = int(os.getenv("SESSION_TIMEOUT", 30))

    def get_secret_key(self) -> str:
        return self.SECRET_KEY

settings = Settings()