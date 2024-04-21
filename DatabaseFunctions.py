import mysql.connector
from UserClass import User

try:
    from ForDebugging import print_database
except:
    print('ForDebugging Module Not Found')


def connect_database():
    #This is just free sample online database so do not even bother messing around :)) 
    connection = mysql.connector.connect(
        host='sql11.freesqldatabase.com',
        user='sql11695288',
        password='Q2xne5YcPF',
        database='sql11695288'
    )
    return connection

def test_database_connection():
    #backup option in case something happens to database and it can not be connected.
    try:
            db = connect_database()
            if db.is_connected():
                print("Connected to MySQL database")
                return True
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return False
    
def create_table(table_name, cursor):
    table = f"""CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Firstname VARCHAR(255),
        Lastname VARCHAR(255),
        Username VARCHAR(255),
        Password VARCHAR(255),
        PC_Score INT,
        User_Score INT
    )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;"""
    cursor.execute(table)
    print(f"{table_name} Table Created")

def table_exists(table_name):
    #Ensures that table exists
    #Since we passed test connection then it is possible to connect. So no need for more testing.
    db = connect_database()

    c = db.cursor()
    c.execute('SHOW TABLES LIKE %s', (table_name,))
    
    if c.fetchone() is None:
        create_table(table_name, c)
    else:
        print(f"Table {table_name} Exists")

def add_single_query(table_name, details):
    db = connect_database()

    c = db.cursor()
    sql = f"INSERT INTO {table_name} (Firstname, Lastname, Username, Password, PC_Score, User_Score) VALUES (%s, %s, %s, %s, %s, %s)"
    c.execute(sql, details)
    
    print('Query added to database succesfully')

    db.commit()
    c.close()
    db.close()

def search_user(table_name, creds):
    db = connect_database()

    cursor = db.cursor()

    sql = f"SELECT * FROM {table_name} WHERE Username = %s AND Password = %s"
    cursor.execute(sql, creds)
    
    row = cursor.fetchone()

    cursor.close()
    db.close()

    if row:
        return User(id=row[0],
                    firstname=row[1],
                    lastname=row[2],
                    username=row[3],
                    password=row[4],
                    user_score=row[5],
                    PC_score=row[6])
    else:
        return None
    

def username_availability(table_name, username):
    try:
        db = connect_database()
        cursor = db.cursor()

        sql = f"SELECT * FROM {table_name} WHERE Username = %s"
        cursor.execute(sql, (username,))
        
        row = cursor.fetchone()
        
        cursor.close()
        db.close()

        if row:
            return False
        else:
            return True
        
    except mysql.connector.Error as e:
        print("Error:", e)
        return True

print_database()