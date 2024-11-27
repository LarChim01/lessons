from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, field_validator
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from operator import attrgetter

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory="templates")


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

users :List[User] = [
    User(id=1, username='UrbanUser', age = 25),
    User(id=2, username='UrbanTest', age = 35),
    User(id=3, username='Capybara', age = 60),
    User(id=4, username='Urban4', age = 55),
]

def get_index(li, target):
    for index, x in enumerate(li):
        if x.id == target:
            return index
    raise HTTPException(status_code=404, detail="Пользователь с таким id не найден")


@app.get("/",  response_class=HTMLResponse)
async def get_all(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_task(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User not found")




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

