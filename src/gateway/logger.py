from __future__ import annotations

import configparser
import logging
import logging.handlers
import sys
from pathlib import Path

def setup_logging(service_name: str = "gateway") -> None:
    config_path = Path(__file__).parent.parent.parent / "config.cfg"  # поднимаемся на 2 уровня до корня
    config = configparser.ConfigParser()
    config.read(config_path)


    # Создаем отдельную папку для логов каждого сервиса
    log_dir = Path("../logs") / service_name
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
