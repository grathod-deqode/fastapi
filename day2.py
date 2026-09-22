from fastapi import FastAPI
#from pydantic import BaseModel

app = FastAPI()


class Product :
    name : str
    price : float
    availabel : bool 
    tag : list[str] = []

    


@app.get("/")
def welcome_pydantic():
    return "welcome pydantic"

