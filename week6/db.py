# import psycopg2


passwd = ""

# # Option 1:

# # conn = psycopg2.connect(
# #     f"postgresql://postgres:{passwd}@.co:5432/postgres?sslmode=require",
# # )

# # Option 2
# conn = psycopg2.connect(
#     host=".co",
#     port="5432",
#     dbname="postgres",
#     user="postgres",
#     password=passwd,
#     sslmode="require",
# )

# with conn, conn.cursor() as cursor:
#     cursor.execute("select current_database(), current_user, now();")
#     print(cursor.fetchone())
    
#     query = "SELECT * FROM actor"
#     cursor.execute(query)
#     results = cursor.fetchall()

# conn.close()

# for item in results:
#     print(item)


import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = "postgres"
PASSWORD = passwd
HOST = "postgres"
PORT = 5432
DBNAME = "di170"

# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")