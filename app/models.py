from typing import Optional ,List
from uuid import UUID ,uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str ,  Enum):
    male="male"
    female="female"

class Roles(str,Enum):
    admin="admin"
    worker="worker"
    student="student"

class User(BaseModel):
    id:Optional[UUID]=uuid4()
    first_name:str
    last_name:str
    middle_name:Optional[str]= None
    gender:Gender #Enum Class is mentioned here
    roles:List[Roles] # one user can have many roles 

class UserUpdateRewuest(BaseModel):
    first_name:Optional[str] = None
    last_name:Optional[str] = None
    middle_name:Optional[str] = None
    gender:Optional[Gender] = None
    roles:Optional[List[Roles]] = None
