## Strawberries Shop
Интернет магазин на django

## Использованные технологии
django
bootstrap
postgres
elasticsearch
nginx
docker
gunicorn

## Подробнее
Реализована регистрация и авторизация. Для авторизованных пользователей доступна история заказов. Для всех пользователей доступны формирование корзины заказов и сам заказ товаров с уведомлением пользователя о состоянии заказа по email. Для авторизации анонимных пользователей используются сессии. Также реализована древовидная структура категорий и подкатегорий.
Сущности в БД:
- User
- Product
- Category
- Cart
- Order
Для продакшен сервера используется контейнерезация всего проекта

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