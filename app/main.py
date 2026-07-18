from fastapi import FastAPI ,HTTPException
from typing import List
from uuid import UUID,uuid4

from models import User,UserUpdateRewuest,Gender,Roles

app = FastAPI()

db: List[User] =[
    User(
    id=UUID("2bf09adb-5aec-451b-85c8-1d1a75d59531"),
    first_name="F-1",
    last_name ="L-1",
    gender=Gender.male,
    roles=[Roles.student]
    ),
    User(
    id=UUID("2bf09adb-5aec-451b-85c8-1d1a75d59532"),
    first_name="F-2",
    last_name ="L-2",
    gender=Gender.female,
    roles=[Roles.admin,Roles.worker]
    )
]

@app.get("/")
async def root():
    return {"Hello":"User"}

@app.get("/api/v1/users")
async def feetch_users():
    return db

@app.post("/api/v1/users")
async def register_users(user:User):
    db.append(user)
    return {"message":"user adedd"}

@app.delete("/api/v1/users/{user_id}")
async def remove_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message":f"id:{user_id}deleted"}
    
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRewuest,  user_id:UUID):
    for user in db:
        if user.id ==user_id:

            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message":"User updated succesfully"}
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exists"
    )
