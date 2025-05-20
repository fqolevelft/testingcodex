from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

# In-memory storage for demonstration
super_admins: Dict[str, str] = {"admin": "admin"}  # username -> password
admins: Dict[str, Dict[str, str]] = {}
companies: List[Dict] = []

class Login(BaseModel):
    username: str
    password: str

class AdminCreate(BaseModel):
    username: str
    password: str

class Company(BaseModel):
    name: str
    address: str
    payday: str

@app.post("/superadmin/login")
def superadmin_login(credentials: Login):
    if super_admins.get(credentials.username) == credentials.password:
        return {"status": "logged_in"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/superadmin/create_admin")
def create_admin(admin: AdminCreate):
    if admin.username in admins:
        raise HTTPException(status_code=400, detail="Admin exists")
    admins[admin.username] = {"password": admin.password, "companies": []}
    return {"status": "admin_created"}

@app.post("/admin/login")
def admin_login(credentials: Login):
    stored = admins.get(credentials.username)
    if stored and stored["password"] == credentials.password:
        return {"status": "logged_in"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/admin/{username}/companies")
def get_companies(username: str):
    admin = admins.get(username)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return admin["companies"]

@app.post("/admin/{username}/companies")
def add_company(username: str, company: Company):
    admin = admins.get(username)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    company_data = company.dict()
    admin["companies"].append(company_data)
    companies.append(company_data)
    return {"status": "company_added"}
