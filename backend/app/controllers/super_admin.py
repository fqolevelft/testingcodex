from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.auth_service import authenticate_super_admin
from ..services.admin_service import create_admin

router = APIRouter(prefix="/api/superadmin")


@router.post("/login")
def login(data: dict):
    if authenticate_super_admin(data.get("email"), data.get("password")):
        return {"message": "super admin logged in"}
    raise HTTPException(status_code=401, detail="invalid credentials")


@router.post("/admins")
def new_admin(data: dict, db: Session = Depends(get_db)):
    admin = create_admin(db, data.get("email"), data.get("password"))
    return {"id": admin.id, "email": admin.email}
