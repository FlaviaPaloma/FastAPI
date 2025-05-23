from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados
class Item(BaseModel):
    name: str
    description: str = None

# Endpoint GET
@app.get("/")
def read_root():
    return {"message": "API funcionando!"}

# Endpoint POST
@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item recebido", "item": item}
