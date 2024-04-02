import mysql.connector
from dotenv import dotenv_values

creds = dotenv_values(".env")

def print_database():
    try:
        db = mysql.connector.connect(
            host=creds['host'],
            user=creds['user'],
            password=creds['password'],
            database=creds['database']
        )
        if db.is_connected():
            print("Connected to MySQL database")
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")

print_database()