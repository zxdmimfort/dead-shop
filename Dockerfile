FROM python:3.11-slim-buster
RUN apt-get update && apt-get install -y netcat
WORKDIR /src
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --only main --no-root --no-directory
COPY entrypoint.sh ./
COPY app/ ./app
RUN poetry install --only main
RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "poetry", "run", "./entrypoint.sh" ]