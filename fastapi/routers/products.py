from fastapi import APIRouter, HTTPException, status
from models.model import Product

router = APIRouter(prefix="/products", tags=["Products"])


products = {
    1: {
        "name": "Laptop",
        "price": 50000,
        "in_stock": True,
        "tags": ["electronics"],
        "category": {
            "name": "Computer",
            "description": "Computer products"
        }
    }
}


@router.get("/{product_id}")
def get_product(product_id: int):

    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[product_id]


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):

    new_id = len(products) + 1

    products[new_id] = product.model_dump()

    return {
        "id": new_id,
        **products[new_id]
    }