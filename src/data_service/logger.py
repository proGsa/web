from __future__ import annotations

import configparser
import logging
import logging.handlers
import sys
import os
from pathlib import Path

def setup_logging(service_name: str = "data_service") -> None:
    config_path = Path(os.getenv("CONFIG_PATH", "/app/config.cfg"))
    config = configparser.ConfigParser()
    if not config.read(config_path):
        print(f"WARNING: config file not found or empty: {config_path}")
        
    root_dir = config_path.parent
    log_dir = root_dir / "logs" / service_name
    # log_dir = Path("../logs") / service_name
    log_dir.mkdir(parents=True, exist_ok=True)

    try:
        log_level = getattr(logging, config["app"].get("LOG_LEVEL", "DEBUG").upper(), logging.DEBUG)
        
        simple_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        detailed_format = "%(asctime)s - %(name)s - %(levelname)s [%(filename)s:%(lineno)d] - %(message)s"
        
        # Базовый логгер
        logger = logging.getLogger()
        logger.setLevel(log_level)
        
        # Консольный обработчик
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(simple_format))
        
        # Файл для debug
        debug_handler = logging.handlers.RotatingFileHandler(
            filename=log_dir / "debug.log",
            maxBytes=10 * 1024 * 1024,
            backupCount=5
        )
        debug_handler.setLevel(log_level)
        debug_handler.setFormatter(logging.Formatter(detailed_format))
        
        # Файл для ошибок
        error_handler = logging.handlers.RotatingFileHandler(
            filename=log_dir / "error.log",
            maxBytes=10 * 1024 * 1024,
            backupCount=5
        )
        error_handler.setLevel(logging.WARNING)
        error_handler.setFormatter(logging.Formatter(detailed_format))
        
        # Добавляем обработчики
        logger.addHandler(console_handler)
        logger.addHandler(debug_handler)
        logger.addHandler(error_handler)
        
        # Настройка логирования для сторонних библиотек
        logging.getLogger("sqlalchemy").setLevel(logging.WARNING)
        logging.getLogger("uvicorn").setLevel(logging.INFO)

    except Exception as e:
        print(f"Ошибка при инициализации логгера: {e}")
        sys.exit(1)
