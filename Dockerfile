# Pull base image
FROM python:3.10.9-bullseye as base

ARG user=app

RUN groupadd $user && useradd --no-log-init -r -g $user $user

WORKDIR /hello

COPY requirements.txt ./
RUN PIP_ROOT_USER_ACTION=ignore pip install --upgrade pip && \
    PIP_ROOT_USER_ACTION=ignore pip install -r requirements.txt

COPY api ./api
ENV PYTHONPATH api

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
