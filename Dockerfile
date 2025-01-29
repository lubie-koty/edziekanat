FROM ghcr.io/astral-sh/uv:latest

ARG HOST
ARG PORT

ADD . /app

WORKDIR /app
RUN uv sync --frozen

CMD uv run fastapi run --host ${HOST} --port ${PORT}
