from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def welcome():
    return "Главная страница!"


@app.get("/user/admin")
async def admin():
    return "Вы вошли как Админ!"

@app.get("/user/{id}")
async def user(id):
    return f"Вы вошли как пользователь № {id}!"


@app.get("/user")
async def info_user(username = 'user' , age = 25):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
