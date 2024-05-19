from fastapi import APIRouter
#importando coneccion con base de datos para poder interactuar
from config.db import conn
#importar schema db
from models.user import users
#importar esquema de Usuario (Clase User)
from schemas.user import User

user = APIRouter()

@user.get("/users")
async def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
async def create_user(user:User):
    print(user)
    return f"hola {user.name}"   

 