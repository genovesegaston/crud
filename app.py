from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.include_router(user)

@app.get("/{nombre}")
async def saludar(nombre:int):
    return f'Hola',nombre