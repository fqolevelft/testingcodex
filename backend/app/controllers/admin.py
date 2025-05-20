from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.auth_service import authenticate_admin

router = APIRouter(prefix="/api/admin")


@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    if authenticate_admin(db, data.get("email"), data.get("password")):
        return {"message": "admin logged in"}
    raise HTTPException(status_code=401, detail="invalid credentials")
