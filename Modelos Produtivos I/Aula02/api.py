from fastapi import FastAPI
from pydantic import BaseModel
import requests


# uvicorn api:app --reload --port 8001

class User(BaseModel):
    nome:str
    idade: int


users = [
    {"nome":"Davi", "idade":30},
    {"nome":"Jeremias", "idade":32},
    {"nome":"Gabi", "idade":15},
]

app = FastAPI()

#--------------------------------------------------------------------------
# informando status
#--------------------------------------------------------------------------

@app.get("/status")
def status() -> dict:
    return {"status":"on"}

#--------------------------------------------------------------------------
# inicializando
#--------------------------------------------------------------------------

@app.get("/users")
def get_users() -> list:
    return users

#--------------------------------------------------------------------------
# incluir usuário
#--------------------------------------------------------------------------

@app.get("/users/{index}")
def get_user_index(index:int) ->dict:
    return users[index]

#--------------------------------------------------------------------------
# alterar usuário
#--------------------------------------------------------------------------

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return{"msg":"Usuário cadastrado!"}

#--------------------------------------------------------------------------
# alterar usuário
#--------------------------------------------------------------------------

@app.put("/users/{index}")
def update_user(index:int, user: User):
    users[index] = user
    return{"msg":"Usuário cadastrado!"}

#--------------------------------------------------------------------------
# deletar usuário
#--------------------------------------------------------------------------

@app.delete("/users/{index}")
def remove_user(index:int):
    users.pop(index)
    return {"msg":"Usuário deletado!"}

def get_experiments():