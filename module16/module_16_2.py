from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

@app.get("/")
async def welcome():
    return "Главная страница!"


@app.get("/user/admin")
async def admin():
    return "Вы вошли как Админ!"

@app.get("/user/{id}")
async def user(id : Annotated[int, Path(le=100, ge =1, description='Enter User ID', example='5')]):
    return f"Вы вошли как пользователь № {id}!"


@app.get("/user/{username}/{age}")
async def info_user(username: Annotated[str, Path(min_length=5,max_length=20,description='Enter username', example='UrbanUser')]
                    , age : Annotated[int, Path(ge=18, le =120, description='Enter User ID', example='24')]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
