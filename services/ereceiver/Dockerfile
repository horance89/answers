# eReceiver Dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY . .

# Create /var/log and set permissions
RUN mkdir -p /var/log && chmod 777 /var/log

RUN pip install flask python-dotenv psycopg2-binary requests

CMD ["python", "app.py"]
