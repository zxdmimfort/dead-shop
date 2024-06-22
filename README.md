## Запуск
Создать .env по образцу example.env
```sh
poetry install
docker compose up
python ./app/manage.py migrate
python ./app/manage.py search_index --rebuild
python ./app/manage.py runserver
```
## Форматирование
```sh
ruff check --fix
ruff format
```