from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@db:5432/appdb"
    SUPER_ADMIN_EMAIL: str = "super@admin.com"
    SUPER_ADMIN_PASSWORD: str = "supersecret"
    ADMIN_EMAIL: str = "admin@admin.com"
    ADMIN_PASSWORD: str = "adminpass"

settings = Settings()
