FROM python:3.10
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src/bet_maker /src/bet_maker
COPY ./alembic ./alembic
COPY alembic.ini alembic.ini