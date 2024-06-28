FROM python:3.11-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y netcat
WORKDIR /src
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --only main --no-root --no-directory
COPY entrypoint.sh ./
COPY app/ ./app
RUN poetry install --only main
RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "poetry", "run", "./entrypoint.sh" ]