import os
# Файл конфигурации Gunicorn

# Количество воркеров (процессов), которые будут обрабатывать запросы.
workers = 4

# Хост и порт, на котором Gunicorn будет слушать входящие соединения.
bind = "127.0.0.1:8000"

# Путь к файлу, в котором будет храниться PID процесса Gunicorn.
pidfile = f"gunicorn_pid.txt"

# Это указывает Gunicorn на путь к вашему проекту Django.
pythonpath = '/home/pavelpc/PycharmProjects/Working_Projects/Django_Casinos_Server'

# Путь к статическим файлам Django (CSS, JavaScript, изображения и т.д.).
# Должен соответствовать настройке STATIC_ROOT в файле настроек Django.
raw_env = "DJANGO_STATIC_PATH=/home/pavelpc/PycharmProjects/Working_Projects/Django_Casinos_Server/casinos_server/static"


# Дополнительные параметры для оптимизации производительности.
max_requests = 1000
timeout = 30
keepalive = 2


# Запуск асинхронного Uvicorn:
# gunicorn my_app.asgi:application -k uvicorn.workers.UvicornWorker -c gunicorn_config.py

# Запуск не асинхронного Gunicorn:
# gunicorn my_app.wsgi:application -c gunicorn_config.py
