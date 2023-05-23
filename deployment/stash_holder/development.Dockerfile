FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./deps/development.requirements.txt /tmp/development.requirements.txt
COPY ./deps/common.requirements.txt /tmp/common.requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/development.requirements.txt

COPY ./app /app
COPY ./configs /app-configs

ENV HOME=/app
ENV PYTHONPATH="${PYTHONPATH}:/"
WORKDIR $HOME