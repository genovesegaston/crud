from fastapi import APIRouter,Response,status
#importando coneccion con base de datos para poder interactuar
from config.db import conn
#importar schema db
from models.user import users
#importar esquema de Usuario (Clase User)
from schemas.user import User
#importar la libreria de criptografia para la contraseña
from cryptography.fernet import Fernet


key = Fernet.generate_key()
f= Fernet(key)
user = APIRouter()
user.tags = ["User"]
user.prefix = "/users"


@user.get("/",response_model=list[User])
async def get_users():
    resultado =   conn.execute(users.select()).fetchall()
    
    return resultado

@user.get("/{id}",response_model=User)
async def get_user(id:int):
    resultado =  conn.execute(users.select().where(users.c.id==id)).first()
    
    return resultado

@user.post("/",response_model=list)
async def create_user(user:User):
    new_user = {"name": user.name,"email":user.email,}
    new_user["password"]=f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values((new_user)))
    #conn.commit()
    
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()   

@user.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id:int):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
@user.put("/{id}",response_model=User)
async def update_user(id:int,user:User):
    conn.execute(users.update().values(name=user.name,email=user.email,password=f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    return user