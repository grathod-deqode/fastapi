from fastapi import FastAPI
#from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def welcome_pydantic():
    return "welcome pydantic"