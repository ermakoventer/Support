#FROM python:3.10
#
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /usr/src/app
#
#COPY requirements.txt ./
#
#RUN pip install --upgrade pip
#
#RUN pip install -r requirements.txt

FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/

RUN pip install poetry

RUN poetry install


