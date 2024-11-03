#Создание БД, добавление, выбор и удаление элементов.
import sqlite3
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

'''
Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:

    id - целое число, первичный ключ
    username - текст (не пустой)
    email - текст (не пустой)
    age - целое число
    balance - целое число (не пустой)
'''


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL

)
''')
#Заполните её 10 записями:


# for i in range(1,11):
#     cursor.execute("INSERT INTO Users (username,email,age, balance) VALUES (?, ?, ?,?) ", (f'User{i}', f'example{i}@gmail.com', f'{i*10}' , '1000'))
#
#Обновите balance у каждой 2ой записи начиная с 1ой на 500:
for i in range(1,11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ? ",(500, f'{i}'))

#Удалите каждую 3ую запись в таблице начиная с 1ой:
for i in range(1,11, 3):
    cursor.execute("DELETE FROM  Users  WHERE id = ? ",( f'{i}',))

#Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
#Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

cursor.execute("SELECT * FROM Users WHERE age != ? ",("60",))
users = cursor.fetchall()

for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]}| Баланс: {user[4]}')









connection.commit()
connection.close()


