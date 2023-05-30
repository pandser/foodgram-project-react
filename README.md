# Дипломный проект Foodgram
![Зелёный - это хорошо!](https://github.com/pandser/foodgram-project-react/actions/workflows/foodgram.yml/badge.svg)

Cайт Foodgram, «Продуктовый помощник». 
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

### Используемые технологии

- Python 3.11
- Django 4.2
- Django Rest Framework 3.14.0
- PostgreSQL
- Nginx
- Docker

### Инструкция для разворачивания проекта на удаленном сервере:
- Склонируйте проект из репозитория:
```bash
git clone git@github.com:pandser/foodgram-project-react.git
```

- Подключитесь к вашему серверу

```bash
ssh <имя пользователя>@<ip вашего сервера>
```

- Установите Docker и docker-compose
```bash
# Установка утилиты для скачивания файлов
sudo apt install curl
# Эта команда скачает скрипт для установки докера
curl -fsSL https://get.docker.com -o get-docker.sh
# Эта команда запустит его
sh get-docker.sh 
# Эта команда скачает все необходимые файлы для установки docker-compose
sudo curl -SL https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
# Даем права на запуск файла docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

- Создайте файл с переменными окружения .env

```bash
touch .env
```

- Пример файла .env

```text
SECRET_KEY=<Секретный ключ для Django>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<пароль к базе данных>
DB_HOST=foodgram-db
DB_PORT=5432
```

- Скопируйте файлы из папки infra/ на ваш удаленный сервер. Предварительно изменив значение server_name в файле nginx.conf

```bash
scp -r infra/* <имя пользователя>@<ip вашего сервера>:/home/<имя пользователя>/
```

- Запустите docker-compose
```bash
sudo docker-compose up
```

- Выполнить следующие команды
```bash
# Собрать и выполнить миграции
sudo docker exec -it foodgram_back python manage.py makemigrations
sudo docker exec -it foodgram_back python manage.py migrate
# Создать суперпользователя
sudo docker exec -it app python manage.py createsuperuser
# Импортировать ингредиенты
sudo docker exec -it app python manage.py importcsv
# Собрать статику
sudo docker exec -it app python manage.py collectstatic --no-input
```

---

### Проект доступен по адресу 
http://158.160.105.109/

доступ к админке

http://158.160.105.109/admin/

login: root (root@ya.ru)

password: root
