import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price 
    
    );
    
    ''')

def get_all_products():
    cursor.execute("SELECT * FROM Products ")
    return cursor.fetchall()

def set_products(id,title, description, price):
    cursor.execute(f'''
    INSERT INTO Products VALUES('{id}','{title}', '{description}', '{price}')
    ''')
    connection.commit()
def close_base():
    connection.commit()
    connection.close()

if __name__ == "__main__":
    tovars = [(1,'Product1', "Первый товар", 100),
              (2, 'Product2', "Второй товар", 200),
              (3,'Product3', "Третий товар", 300),
              (4,'Product4', "Четвёртый товар", 400)]



    initiate_db()

    for item in tovars:
        set_products(item[0],item[1],item[2],item[3])


    spisok = get_all_products()
    print(spisok)

    close_base()
