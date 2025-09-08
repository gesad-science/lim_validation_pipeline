FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir sqlalchemy psycopg2-binary 

COPY ./src ./src

CMD python -m src.db.db && python -m src.main