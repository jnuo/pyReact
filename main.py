from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age:int 

DB: List[Person] = [
    Person(id=1, name="Jamilah", age=22),
    Person(id=2, name="Alex", age=19),
    Person(id=3, name="Ali", age=15)
]

@app.get("/api")
def read_root():
    return DB


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


####
## Venv
####
# Create Virtual Environment        >python3 -m venv .venv
# Activate Virtual Environment      >source .venv/bin/activate
# Install a package into the Env    >python3 -m pip install openpyxl
# De-activate Virtual Environment   >deactivate

# to start frontend                 >npm start
# to start backend                  >uvicorn main:app --reload
