# eProcessor Dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY . .

RUN pip install flask psycopg2-binary python-dotenv requests

CMD ["python", "app.py"]
