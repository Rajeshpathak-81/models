from fastapi import FastAPI
from pydantic import BaseModel
from utils import get_llm_response
# Initialize FastAPI
app = FastAPI()

# Define your data model for Product
class Order(BaseModel):
    product: str
    units: int

class Product(BaseModel):
    name: str
    notes: str

class Userquery(BaseModel):
    query: str
   

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get("/hello")
async def hello_endpoint(name: str = 'World'):
    return {"message": f"Hello, {name}!"}

@app.post("/answers")
async def generate_answers(input:Userquery):
    description = get_llm_response(f"{input.query}")
    return {"answer": description}