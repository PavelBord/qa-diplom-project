FROM mcr.microsoft.com/playwright/python:v1.60.0-noble

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY . .

CMD ["uv", "run", "pytest", "-v"]