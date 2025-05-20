from sqlalchemy.orm import Session
from ..config.settings import settings
from ..models.user import SuperAdmin, Admin


def authenticate_super_admin(email: str, password: str) -> bool:
    return email == settings.SUPER_ADMIN_EMAIL and password == settings.SUPER_ADMIN_PASSWORD


def authenticate_admin(db: Session, email: str, password: str) -> bool:
    admin = db.query(Admin).filter_by(email=email, password=password).first()
    return admin is not None
