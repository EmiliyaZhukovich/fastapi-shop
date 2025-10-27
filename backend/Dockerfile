FROM python:3.11-slim

WORKDIR /app

# Устанавливаем Poetry
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:${PATH}"

# Копируем файлы Poetry
COPY backend/pyproject.toml backend/poetry.lock ./

# Устанавливаем зависимости через Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Копируем остальной код приложения
COPY backend/ .

# Создаем директорию static в правильном месте
RUN mkdir -p static/images

RUN chmod -R 755 static

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
