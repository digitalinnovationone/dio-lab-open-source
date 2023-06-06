from fastapi import FastAPI
from pydantic import BaseModel
import requests 
import mlflow 

# uvicorn api:app --reload --port 8001


class User(BaseModel):
    nome: str 
    idade: int


class Flor(BaseModel):
    sepal_length:float
    sepal_width:float
    petal_length:float
    petal_width:float

# [('sepal_length',12.5),('sepal_width',12.5)]


users = [
    {"nome": 'davi', "idade": 30},
    {"nome": 'jeremias', "idade": 32},
    {"nome": 'ana', "idade": 15}
]

app = FastAPI()


@app.get("/status")
def status() -> dict:
    return {"status": "on"}


@app.get("/users")
def get_users() -> list:
    return users


@app.get("/users/{index}")
def get_user_index(index:int) -> dict:
    return users[index]


@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"msg":"Usuário cadastrado!"}


@app.put("/users/{index}")
def update_user(index:int, user:User):
    users[index] = user
    return {"msg":"Usuário atualizado!"}


@app.delete("/users/{index}")
def remove_user(index:int):
    users.pop(index)
    return {"msg":"Usuário apagado!"}


@app.get("/experiments")
def get_experiments():
    url = 'http://127.0.0.1:5000/api/2.0/preview/mlflow/experiments/list'
    response = requests.request('GET', url=url)
    dados = response.json()
    return dados


@app.post("/model")
def predict(flor: Flor):
    mlflow.set_tracking_uri(uri='http://localhost:5000/')
    PATH = 'models:/Iris/Production'
    classes = ['Setosa', 'Versicolor', 'Virginica']
    loaded_model = mlflow.sklearn.load_model(PATH)

    dados = [[f[1] for f in flor]]
    label = loaded_model.predict(dados) #list array [[],[],[]]

    resultado = classes[int(label[0])]
    return {'class': resultado}


