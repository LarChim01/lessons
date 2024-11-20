import sqlite3
global connection, cursor



connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    global cursor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price

    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    
    );
    ''')


def get_all_products():
    cursor.execute("SELECT * FROM Products ")
    return cursor.fetchall()

def set_products(title, description, price):
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?,?,?)' ,(title, description, price))

    connection.commit()

def is_included(username):
    cursor.execute('SELECT  * FROM Users WHERE username = ?',(username,))
    return True if cursor.fetchone() else False
def set_users( username, email, age, balance=1000):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?,?)', (username, email, age,balance))
    connection.commit()
    # cursor.execute("SELECT * FROM Users ")





def close_base():
    connection.commit()
    connection.close()

if __name__ == "__main__":
    tovars = [(1,'Product1', "Первый товар", 100),
              (2, 'Product2', "Второй товар", 200),
              (3,'Product3', "Третий товар", 300),
              (4,'Product4', "Четвёртый товар", 400)]
    users = [(1, )

    ]


    # connect()
    initiate_db()

    # for item in tovars:
    #     set_products(item[1],item[2],item[3])

    # set_users('newuser2','test@mail.ru',44,)
    # spisok = get_all_products()
    # print(spisok)

    print(is_included('newus2'))


    close_base()