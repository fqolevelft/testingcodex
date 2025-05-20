# FastAPI Admin Dashboard Example

This project provides a small scaffold for a future admin system. It uses
FastAPI for the backend with a PostgreSQL database and React on the
frontend. Docker Compose orchestrates the services.

## Services
- **backend** – FastAPI application with SQLAlchemy models and Alembic
  migrations.
- **db** – PostgreSQL database storing admins and companies.
- **frontend** – React application served by Nginx.

## Running
```bash
docker-compose up --build
```
The frontend will be available at `http://localhost:3000` and API at
`http://localhost:8000`.
