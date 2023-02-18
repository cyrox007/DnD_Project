# PostgreSQL
## Установка
``` bash
sudo apt -y install postgresql
```
## Конфигурация
```
\conninfo
```
## Настрока БД
``` bash
sudo -iu postgres psql -c "alter user postgres with password 'postgres';"
sudo -iu postgres psql -c "create database dnddbase;"
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