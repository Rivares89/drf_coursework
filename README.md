В проекте реализована бэкенд-часть SPA веб-приложения, в котором реализован трекер полезных привычек

В проекте:
Настроен CORS.
Настроена интеграция с Телеграмом.
Реализована пагинация.
Использованы переменные окружения.
Все необходимые модели описаны или переопределены.
Все необходимые эндпоинты реализовали.
Настроили все необходимые валидаторы.
права доступа заложены.
Настроена отложенная задача через Celery.
Проект покрыт тестами как минимум на 80%.
Код оформлен в соответствии с лучшими практиками.
Имеется список зависимостей.
Результат проверки Flake8 равен 100%, при исключении миграций.
Решение выложили на GitHub.
Перед запуском web-приложения: создайте базу данных, создайте и примените миграции, установите необходимые пакеты из файла requirements.txt, заполните файл .env по образцу .env.sample. Используйте команду "python manage.py csu" для создания суперпользователя. Для запуска используйте команду "python manage.py runserver".

Создать образы и контейнеры DOCKER с помощью команд: "docker-compose build" и "docker-compose up".