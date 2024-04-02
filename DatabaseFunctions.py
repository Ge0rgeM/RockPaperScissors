# import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# def print_database():
#     try:
#         db = mysql.connector.connect(
#             host=os.environ.get('host'),
#             user=os.environ.get('user'),
#             password=os.environ.get('password'),
#             database=os.environ.get('database')
#         )
#         if db.is_connected():
#             print("Connected to MySQL database")
#     except mysql.connector.Error as e:
#         print(f"Error connecting to MySQL database: {e}")
print(os.environ.get('host'))
# print_database()