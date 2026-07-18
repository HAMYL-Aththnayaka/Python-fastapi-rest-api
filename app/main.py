from fastapi import FastAPI
from typing import List
from uuid import uuid4

from models import User,Gender,Roles

app = FastAPI()

db: List[User] =[
    User(
    id=uuid4(),
    first_name="F-1",
    last_name ="L-1",
    gender=Gender.male,
    roles=[Roles.student]
    ),
    User(
    id=uuid4(),
    first_name="F-2",
    last_name ="L-2",
    gender=Gender.female,
    roles=[Roles.admin,Roles.worker]
    )
]

@app.get("/")
async def root():
    return {"Hello":"User"}

@app.get("/api/V1/users")
async def feetch_users():
    return db