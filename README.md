# Проект api_yamdb

### Описание проекта:

Проект сбирает отзывы и оценки на произведения. Произведения делятся на категории. 
У произведения может быть 1 или несколько жанров. 

### Благодаря этому проекту аутентифицированные пользователи  могут:
- Оставлять отзывы и давать оценку произведениям (целое число от 1 до 10)
- Оставлять комментарии на отзывы других пользователей

### Пользовательские роли и права доступа:
- Просмотр отзывов, рейтингов и комментариев доступен всем пользователям, аутентифицикация не обязательна
- Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи
- Добавлять произведения, категории и жанры может только администратор
- Удалять отзывы и комментарии могут только модераторы и администраторы
- Полные  полные права на управление всем контентом проекта имеет только администратор

### Порядок регистрации пользователей:
- Пользователь отправляет POST-запрос с параметрами email и username на эндпоинт /api/v1/auth/signup/
- Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email
- Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен)

В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.

### Технологии:

- Python 3.7.9
- Django 3.2
- Gunicorn 20.0.4
- Djangorestframework 3.12.4
- Docker

### Запуск проекта в dev-режиме:
- Установите и активируйте виртуальное окружение:
python3 -m venv venv
source venv/bin/activate

- Установите зависимости из файла requirements.txt:
pip3 install -r requirements.txt

- Примените миграции:
python3 manage.py makemigrations
python3 manage.py migrate

- Запустите сервер:
python3 manage.py runserver

- Использовать проект можно при помощи Postman
- После запуска проекта документация к API будет доступна по адресу http://127.0.0.1:8000/redoc/

### Запуск проекта с помщью Docker:
 - Создайте и запустите образы, контейнеры и тома с помощью:
 docker-compose up
- Выполните миграции:
docker-compose exec web python manage.py migrate
- Загрузите статику:
docker-compose exec web python manage.py collectstatic --no-input
- Создайте суперюзера для управления через страницу администратора
docker-compose exec web python manage.py createsuperuser
- Остановка работы контейнеров без их удаления:
docker-compose stop
- Запуск оставновленных контейнеров
docker-compose start

<details open>
 <summary>Примеры запросов</summary> 
 
Примеры запросов для неавторизованных пользователей:  
Запрос на получение списка всех произведений:  
GET http://127.0.0.1:8000/api/v1/titles/  
Ответ:  
{  
"count": 0,  
"next": "string",  
"previous": "string",  
"results": [  
{  
"id": 0,  
"name": "string",  
"year": 0,  
"rating": 0,  
"description": "string",  
"genre": [],  
"category": {}  
}  
]  
}  

Запрос на получение информации по 1 произведению:  
GET http://127.0.0.1:8000/api/v1/titles/{titles_id}/  
Ответ:  
{  
"id": 0,  
"name": "string",  
"year": 0,  
"rating": 0,  
"description": "string",  
"genre": [  
{  
"name": "string",  
"slug": "string"  
}  
],  
"category": {  
"name": "string",  
"slug": "string"  
}  
}  

Примеры запросов для авторизованных пользователей:  

Запрос на добавление нового отзыва:  
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/  
Ответ:  
{  
"text": "string",  
"score": 1  
}  

Запрос на добавление комментария к отзыву:  
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/  
### Ответ:  
{  
"text": "string"  
}  
</details>

### Проект выполнила:

 **Ольга Жолудева**
