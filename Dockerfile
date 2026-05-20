# Используем официальный образ Python
FROM python:3.11-slim

# Отключаем буферизацию вывода и создание файлов .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Собираем статические файлы Django
RUN python manage.py collectstatic --noinput

# Запускаем Gunicorn (сервер для продакшена)
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]