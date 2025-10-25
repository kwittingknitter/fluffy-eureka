FROM python:3.10
WORKDIR /app

COPY requirements-service.txt .
RUN pip install -r requirements-service.txt

COPY /service ./service
COPY /data ./data
EXPOSE 3000

CMD ["flask", "--app", "service/application", "run", "--host=0.0.0.0", "--port", "3000"]