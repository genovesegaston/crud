from fastapi import FastAPI
from routes.user import user
from schemas.user import User
from config.db import conn
from sqlalchemy import select
app = FastAPI(
    version="1.0",
    
    title="Documentación api",
    description="Gestion y control de backend",
    openapi_tags=[{
        "name":"Users",
        "description":"Gestión de usuarios"
    }]
)

app.include_router(user)

