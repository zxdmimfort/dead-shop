## Запуск
```sh
poetry install
python ./app/manage.py migrate
python ./app/manage.py runserver
```
## Форматирование
```sh
ruff check --fix
ruff format
```