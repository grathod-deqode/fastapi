from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home() :
    return {"message" : "Hello FastAPI"}


@app.get("/items/{item_id}")
def get_items(item_id : int):
    return {"item_id" : item_id}