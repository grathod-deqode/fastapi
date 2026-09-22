from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel) :
    name : str
    price : float
    availabel : bool 
    tags : list[str] = []

products = [
    Product(
        name="Laptop",
        price=50000,
        availabel=True,
        tags=["device", "computer"]
    ),
    Product(
        name="Mouse",
        price=800,
        availabel=True,
        tags=["device", "parts"]
    ),
    Product(
        name="Keyboard",
        price=1500,
        availabel=False,
        tags=["device", "parts"]
    )
]

@app.post("/products")
def create_product(product : Product):
    return product

@app.get("/products" ,response_model=list[Product])
def get_products():
    return products 


@app.get("/")
def welcome_pydantic():
    return "welcome pydantic"

