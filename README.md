# Django, React with Docker, featuring CI/CD

The aim of this project is to create a boilerplate for a Django application with optional React integration, using Docker for both production and development environments. This setup allows for a quick project spin-up and includes CI/CD integration with GitHub workflows.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [CI/CD Integration](#cicd-integration)
- [Future Work](#future-work)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Docker
- Docker Compose
- Git
- Python => 3.9
- NodeJS

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mwangihub/django-react-docker-ci.git
   cd project
   ```

2. **Set up environment variables:**
   Create your environment variable files in the `.envs/.local/` directory. You should have:

   - `.django`
   - `.postgres`

   Example for `.django`:

   ```env
   DEBUG=1
   SECRET_KEY=your_secret_key
   DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
   ```

   Example for `.postgres`:

   ```env
   POSTGRES_DB=your_db_name
   POSTGRES_USER=your_db_user
   POSTGRES_PASSWORD=your_db_password
   ```

## Running the Project

1. **Build and run the Docker containers:**

   ```bash
   docker-compose -f docker-compose.local.yml up --build
   ```

2. **Access the application:**
   - Django: `http://localhost:8000`

## Project Structure

```
project/
├── app/
│   ├── templates/
│   ├── static/
│   ├── app1/
├── tests/
├── settings/
│   ├── settings/
├── react/
├── docker/
│   ├── local/
│   │   ├── django/
│   │   │   └── Dockerfile
│   ├── production/
│   │   └── postgres/
│   │       └── Dockerfile
├── .envs/
│   └── .local/
│       ├── .django
│       └── .postgres
├── manage.py
├── requirements.txt
└── docker-compose.local.yml
```

### `docker-compose.local.yml`

```yaml
volumes:
  project_local_postgres_data: {}
  project_local_redis_data: {}

services:
  django: &django
    build:
      context: .
      dockerfile: docker/local/django/Dockerfile
    image: project_local_django
    container_name: project_local_django
    depends_on:
      - postgres
      - redis
    volumes:
      - .:/app:z
    env_file:
      - ./.envs/.local/.django
      - ./.envs/.local/.postgres
    ports:
      - "8000:8000"
    command: /start

  postgres:
    build:
      context: .
      dockerfile: docker/production/postgres/Dockerfile
    image: project_production_postgres
    container_name: project_local_postgres
    volumes:
      - project_local_postgres_data:/var/lib/postgresql/data
    env_file:
      - ./.envs/.local/.postgres

  redis:
    image: docker.io/redis:6
    container_name: project_local_redis
    volumes:
      - project_local_redis_data:/data

  celeryworker:
    <<: *django
    image: project_local_celeryworker
    container_name: project_local_celeryworker
    depends_on:
      - redis
      - postgres
    ports: []
    command: /start-celeryworker
```

## CI/CD Integration

The project includes CI/CD integration with GitHub workflows. This setup will be added soon to automate the build, test, and deployment processes.

## Future Work

- Configure Docker for the production environment.
- Integrate React frontend (optional).
- Add GitHub workflows for CI/CD.

Feel free to contribute and make suggestions to improve this project!

#### [Go up 👆](#table-of-contents)
