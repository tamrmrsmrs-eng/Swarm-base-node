FROM python:3.11-slim

WORKDIR /app

COPY swarm-core/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY swarm-core/ .

RUN pip install gunicorn

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
