# syntax=docker/dockerfile:1

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copiar o script wait-for-it.sh e garantir permissões de execução
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

CMD ["/wait-for-it.sh", "db:5432", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
