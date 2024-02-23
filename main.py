from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx import Jinja
from pydantic import BaseModel

app = FastAPI()
jinja = Jinja(Jinja2Templates(directory="templates"))

class User(BaseModel):
    name: str

app.users = [
    {"name": "Person1"},
    {"name": "Person2"},
    {"name": "Person3"},
]

@app.get("/")
@jinja.page("index.html")
async def index() -> None:
    return {
        "title": "Python Htmx FastAPI Example",
        "users": app.users
    }
    

@app.get("/users")
@jinja.hx("user-list.html")
async def users() -> list[User]:
    return {"users": app.users}



