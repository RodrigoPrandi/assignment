FROM tiangolo/uvicorn-gunicorn:python3.7

WORKDIR /app/

LABEL maintainer="Fuelsave <areis@fuelsave.io>"

### Copy over and install the requirements
COPY ./src/app/requirements.txt $DIR/
RUN pip install -r $DIR/requirements.txt

COPY ./src /app
ENV PYTHONPATH=/app