from fastapi import APIRouter
#importando coneccion con base de datos para poder interactuar
from config.db import conn
#importar schema db
from models.user import users

user = APIRouter()

@user.get("/users")
async def get_users():
    return conn.execute(users.select().fetch_all())

@user.get("/us")
async def saludar():
    return "Hola bienvenido"    

@user.get("/usa")
async def saludar():
    return "Hola bienvenido"    

@user.get("/use")
async def saludar():
    return "Hola bienvenido"    