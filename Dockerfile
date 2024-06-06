FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV DB_NAME='bankdb'
ENV DB_USER='django'
ENV DB_PASSWORD='xxxxx'
ENV DB_HOST='xxxxx'

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]