from fastapi import FastAPI, status, Body, HTTPException, Path
from pydantic import BaseModel, field_validator
from typing import List, Annotated
from operator import attrgetter

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str = 'UrbanUser'
    age: int = 20

    @field_validator('age')
    def check_age(cls, value):
        if value < 18:
            raise ValueError('Возраст должен быть больше 18 лет')
        elif value > 120:
            raise ValueError('Возраст не может быть больше 120 лет')
        return value


def get_index(li, target):
    for index, x in enumerate(li):
        if x.id == target:
            return index
    raise HTTPException(status_code=404, detail="Пользователь с таким id не найден")


@app.get("/user")
async def get_all() -> List[User]:
    return users


@app.post('/user')
async def insert_user(user: User) -> str:
    try:
        max_id = max(users, key=attrgetter('id')).id
    except:
        max_id = 0
    user.id = max_id + 1
    users.append(user)

    return f"User {user.id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=120, description='Enter User ID', example='2')]
                      , username: Annotated[
            str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')]
                      , age: Annotated[int, Path(ge=18, le=120, description='Enter Age', example='24')]) -> User:
    try:
        ind = get_index(users, user_id)
        old_user = users[ind]
        users[ind].username = username
        users[ind].age = age
        return users[ind]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def user_delete(user_id: Annotated[int, Path(ge=1, le=120, description='Enter User ID', example='2')]) -> User:
    try:
        ind = get_index(users, user_id)
        user = users[ind]
        users.pop(ind)
        return user
        #return f'User №{user_id} is deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/")
def kill_users_all() -> str:
    users.clear()
    return "All users deleted!"
    
