FROM python:3.10
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /service ./service
COPY /data/sessions.json .
EXPOSE 3000

CMD ["flask", "--app", "service", "run", "--host=0.0.0.0", "--port", "3000"]