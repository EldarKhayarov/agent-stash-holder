FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./deps/test.requirements.txt /tmp/test.requirements.txt
COPY ./deps/common.requirements.txt /tmp/common.requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/test.requirements.txt

COPY ./app /app
COPY ./configs /app-configs

ENV HOME=/app
ENV PYTHONPATH="${PYTHONPATH}:/"
WORKDIR $HOME

RUN chmod +x ./start-tests.sh
CMD ["./start-tests.sh"]