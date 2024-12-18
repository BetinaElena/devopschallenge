from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definición del modelo de datos
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
async def read_root():
    return {"message": "¡Hola, Devops Challenge desde FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# Nuevo endpoint para crear un artículo
@app.post("/items/")
async def create_item(item: Item):
    return item
