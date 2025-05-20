from fastapi import FastAPI
from .controllers import hello, super_admin, admin

app = FastAPI()

app.include_router(hello.router)
app.include_router(super_admin.router)
app.include_router(admin.router)
