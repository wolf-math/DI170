
import requests
import json
import sqlite3
from faker import Faker
from time import time

def create_table():
    connection = sqlite3.connect("jokes.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jokes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            joke TEXT NOT NULL
        );
    """)
    connection.commit()
    connection.close()

def get_jokes(n):
    for i in range(n):
        print(i + 1)
        url = 'https://api.chucknorris.io/jokes/random'
        data = requests.get(url)
        data = data.json()
        joke = data['value']
        joke = joke.replace("'", "")
        connection = sqlite3.connect('jokes.db')  #Make a connection to the database
        cursor = connection.cursor() #Think of the cursor as the place that executes queries
        query = f"INSERT INTO jokes (joke) VALUES ('{joke}');"
        cursor.execute(query)  #Cursor runs the query
        connection.commit()  #Finalize the result. "Write" it to the DB
        # results = cursor.fetchall() #Fetch theh results back from the cursor into python variable
        connection.close()  #Close the connection

def gen_fake_data(n):
    start = time()
    f = Faker()
    connection = sqlite3.connect('jokes.db')  #Make a connection to the database
    cursor = connection.cursor() #Think of the cursor as the place that executes queries
    for i in range(n):
        print(i + 1)
        name = f.name()
        query = f"INSERT INTO jokes (joke) VALUES ('{name}');"
        cursor.execute(query)  #Cursor runs the query
    connection.commit()  #Finalize the result. "Write" it to the DB
    connection.close()
    end = time()
    print(f"The function ran in {round(end-start,2)}s")


def view_jokes(limit=5):
    connection = sqlite3.connect("jokes.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM jokes ORDER BY id DESC LIMIT {limit}")
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    print(results)

create_table()
# get_jokes(5)
# gen_fake_data(4)
view_jokes(20)
