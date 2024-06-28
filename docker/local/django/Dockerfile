# Yet Another Markup Language

# Base image with Python
FROM python:3.12.4-slim-bookworm as base

# Common environment settings
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Builder stage to create Python wheels
FROM base as builder

# Install build dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and create wheels
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip wheel --wheel-dir /wheels -r requirements.txt

# Final stage to run the application
FROM base as final

# Set environment variable for build environment
ENV BUILD_ENV local

# Install runtime dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy wheels and install dependencies
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* && rm -rf /wheels

# ------------------------ PostgreSQL ----------------------------------------------
COPY ./docker/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint

# ------------------------ PostgreSQL ----------------------------------------------
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start


COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker && chmod +x /start-celeryworker

COPY ./docker/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat && chmod +x /start-celerybeat

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower && chmod +x /start-flower

# copy application code to WORKDIR
COPY . /app/

ENTRYPOINT ["/entrypoint"]