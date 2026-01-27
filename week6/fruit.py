import sqlite3
from tabulate import tabulate

def order():
    choice = input("What type of shake do you want? ")
    while choice != "X":
        print("Moti's Fruit Shake Stand with questionable hygiene")
        inv = get_inv()
        print(tabulate(inv, headers=['Fruit', 'Amount']))
        choice = input("What do you want to add to your shake?")
        update_inv(choice)
    else:
        print("Bye")

def update_inv(choice):
    query = f"UPDATE fruit SET quantity=quantity-1 WHERE fruit = '{choice}';"
    return run_query(query)

def get_inv():
    query = "SELECT fruit, quantity FROM fruit ORDER BY fruit ASC;"
    return run_query(query)

def run_query(query):
    connection = sqlite3.connect("shakes.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results

def createdb(tname):
    query = f"""
        CREATE TABLE IF NOT EXISTS {tname}(
        fruit_id INTEGER SERIAL PRIMARY KEY,
        fruit varchar(50) UNIQUE,
        quantity INT NOT NULL DEFAULT 0
        )
    """
    return run_query(query)

def addinv(fruit, amount):
    query = f"""
        INSERT INTO fruit (fruit, quantity)
        VALUES ({fruit}, {amount})
        ON CONFLICT({fruit}) DO UPDATE SET
        quantity = quantity + excluded.quantity;
    """

    return run_query(query)


run_query("DROP TABLE fruit;")
createdb('fruit')
addinv('banana','15')

addinv('apple','25')
addinv('pear','10')
addinv('strawberry','8')

print(get_inv())

# order()