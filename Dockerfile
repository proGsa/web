FROM python:3.13-slim AS builder

# Переменные окружения
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VERSION=2.1.1 \
    PATH="$POETRY_HOME/bin:$PATH" \
    PYTHONPATH=/app/src

# Рабочая директория
WORKDIR /app

# Установка системных зависимостей и Poetry
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python - \
    && chmod +x /opt/poetry/bin/poetry

ENV PATH="/opt/poetry/bin:$PATH"

COPY pyproject.toml poetry.lock ./

# Установка зависимостей без виртуального окружения
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi
# Копируем остальной проект
COPY . .

# --- Финальный рантайм-образ ---
FROM python:3.13-slim

ENV PYTHONPATH=/app/src \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH"

WORKDIR /app

# Копируем зависимости и бинарники
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Копируем Poetry
COPY --from=builder /opt/poetry /opt/poetry

# Копируем исходный код
COPY . .

# Линтинг и типизация
RUN poetry run ruff check --fix ./src
RUN poetry run mypy ./src

# Запуск приложения
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
