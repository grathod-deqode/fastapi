from pydantic import BaseModel


class Category(BaseModel):
    name: str
    description: str


class Product(BaseModel):
    name: str
    price: int
    in_stock: bool
    tags: list[str]
    category: Category