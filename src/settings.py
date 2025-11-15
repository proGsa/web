# from __future__ import annotations

# import configparser
# import os


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# config = configparser.ConfigParser()
# config.read(os.path.join(BASE_DIR, 'config.cfg'))


# class Settings:
#     def __init__(self) -> None:
#         app = config["app"]

#         self.DATABASE_URL_ASYNC: str = app["DATABASE_URL_ASYNC"]
#         self.SECRET_KEY: str = app["SECRET_KEY"]
#         self.ALGORITHM: str = app.get("ALGORITHM", "HS256")
#         self.SESSION_TIMEOUT: int = int(app.get("SESSION_TIMEOUT", 30))

#     def get_secret_key(self) -> str:
#         return self.SECRET_KEY


# settings = Settings()
from __future__ import annotations
import os

class Settings:
    def __init__(self) -> None:
        # Определяем, используется ли реплика (mirror)
        self.USE_MIRROR: bool = os.getenv("USE_MIRROR", "false").lower() == "true"
        self.DB_MODE: str = os.getenv("DB_MODE", "write")  # write или read
        self.NODE_NAME: str = os.getenv("NODE_NAME", "app_main")

        # Настройки БД - используем одного пользователя для всего
        self.DB_USER: str = os.getenv("DB_USER", "write_user")
        self.DB_PASSWORD: str = os.getenv("DB_PASSWORD", "write_password")
        self.DB_NAME: str = os.getenv("DB_NAME", "mydb")
        self.DB_PORT: str = os.getenv("DB_PORT", "5432")
        
        # Хосты для master и slave
        self.DB_MASTER_HOST: str = os.getenv("DB_HOST", "db-master")
        self.DB_SLAVE_HOST: str = os.getenv("DB_SLAVE_HOST", "db-slave")

        # DATABASE_URL_ASYNC выбирается автоматически
        if self.USE_MIRROR and self.DB_MODE == "read":
            # Для read-операций используем slave
            self.DATABASE_URL_ASYNC = (
                f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_SLAVE_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            )
        else:
            # Для write-операций и по умолчанию используем master
            self.DATABASE_URL_ASYNC = (
                f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_MASTER_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            )

        # Остальные настройки приложения
        self.SECRET_KEY: str = os.getenv("SECRET_KEY", "mysecret")
        self.ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
        self.SESSION_TIMEOUT: int = int(os.getenv("SESSION_TIMEOUT", 30))

    def get_secret_key(self) -> str:
        return self.SECRET_KEY

settings = Settings()