from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel) :
    name : str
    price : float
    availabel : bool 
    tag : list[str] = []

@app.post("/products")
def create_product(product : Product):
    return product


@app.get("/")
def welcome_pydantic():
    return "welcome pydantic"

