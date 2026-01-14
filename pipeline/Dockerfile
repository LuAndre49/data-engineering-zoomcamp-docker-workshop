#FROM python:3.13.11-slim

#RUN pip install pandas pyarrow
FROM python:3.13.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code

ENV PATH="/code/.venv/bin:$PATH"

COPY ".python-version" "uv.lock" "pyproject.toml" ./

RUN uv sync --locked

COPY ingest_data.py ingest_data.py

ENTRYPOINT ["python", "ingest_data.py"]