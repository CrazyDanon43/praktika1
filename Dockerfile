FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /praktika1
RUN pip install poetry

RUN pip install --no-cache-dir fastapi uvicorn

COPY . .

RUN poetry install --no-root

ENV PYTHONPATH="/src:$PYTHONPATH"

EXPOSE 80

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"]
