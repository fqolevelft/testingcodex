from sqlalchemy.orm import Session
from ..models.user import Admin


def create_admin(db: Session, email: str, password: str) -> Admin:
    admin = Admin(email=email, password=password)
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin
