#Домашнее задание по теме "Выбор элементов и функции в SQL запросах"
import sqlite3
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()




cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL

)
''')
# #Заполните её 10 записями:
#
#
# # for i in range(1,11):
# #     cursor.execute("INSERT INTO Users (username,email,age, balance) VALUES (?, ?, ?,?) ", (f'User{i}', f'example{i}@gmail.com', f'{i*10}' , '1000'))
# #
# #Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# for i in range(1,11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ? ",(500, f'{i}'))
#
# #Удалите каждую 3ую запись в таблице начиная с 1ой:
# for i in range(1,11, 3):
#     cursor.execute("DELETE FROM  Users  WHERE id = ? ",( f'{i}',))
#
# #Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# #Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
#
# cursor.execute("SELECT * FROM Users WHERE age != ? ",("60",))
# users = cursor.fetchall()
#
# for user in users:
#     print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]}| Баланс: {user[4]}')



#Удалите из базы данных not_telegram.db запись с id = 6

cursor.execute("DELETE FROM  Users  WHERE id = ? ",('6',))

#Подсчитать общее количество записей.
cursor.execute("SELECT COUNT(*) FROM Users")
all_users = cursor.fetchone()[0]
print(all_users)


#Посчитать сумму всех балансов.

cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]
print(all_balance)

#Вывести в консоль средний баланс всех пользователей.
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)




connection.commit()
connection.close()
