# PostgreSQL
## Установка
``` bash
sudo apt -y install postgresql
```
## Конфигурация
```
\conninfo
```
## Старт
``` bash
sudo service postgresql start
```
## Настрока БД
``` bash
sudo -iu postgres psql -c "alter user postgres with password 'postgres';"
sudo -iu postgres psql -c "create database dnddbase;"
```
# Миграции
``` bash
alembic init alembic
```
## Генерация новых миграций
``` bash
alembic revision --message="Initial" --autogenerate
```
## Применение миграций
``` bash
alembic upgrade head
```
# Redis
## Установка и запуск
``` bash
sudo apt-get update
sudo apt-get install redis
sudo apt-get install redis-server
sudo service redis-server start
```
## Проверить
``` bash
redis-cli
```
## Запуск сервера
``` bash
celery -A run_celery worker -B
```