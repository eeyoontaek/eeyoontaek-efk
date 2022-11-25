from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Info(BaseModel):
    username: str
    phone_number: str

@app.get("/")
def home_view():
    return  "홈페이지"

@app.get("/first")
def first_page():
    return "첫 번째 페이지"

@app.get("/second")
def second_page():
    return "두 번째 페이지"

@app.post("/Info")
def info_page(info: Info):
    return info