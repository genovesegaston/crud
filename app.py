from fastapi import FastAPI
from routes.user import user
from schemas.user import User
from config.db import conn
from sqlalchemy import select
app = FastAPI()

app.include_router(user)

""" @app.get("/user")
async def get_user():
   return conn.execute(select()).fetchall()
     

@app.post("/user")
async def  create_user(user:User):
    print(user)
    return ("se a creado el usuario") """