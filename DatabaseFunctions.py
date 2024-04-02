import mysql.connector

def print_database():
    try:
        #This is just free sample online database so do not even bother messing around :)) 
        db = mysql.connector.connect(
            host='sql11.freesqldatabase.com',
            user='sql11695288',
            password='Q2xne5YcPF',
            database='sql11695288'
        )
        if db.is_connected():
            print("Connected to MySQL database")
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")

print_database()