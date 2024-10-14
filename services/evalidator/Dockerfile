# eValidator Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install flask python-dotenv psycopg2-binary requests

CMD ["python", "app.py"]
