FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# minimal system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    make \
 && rm -rf /var/lib/apt/lists/*

# install uv
RUN python -m pip install --no-cache-dir uv

# copy dependency metadata first (cache-friendly)
COPY pyproject.toml uv.lock ./

# create venv + install deps only (no project yet, since code isn't copied)
RUN uv sync --frozen --no-dev --no-install-project

# now copy the project code
COPY . .

# install your project into the venv
RUN uv pip install -e .

# default command (CLI)
CMD ["make", "demo"]
