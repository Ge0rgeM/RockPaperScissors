import mysql.connector

def test_database_connection():
    #backup option in case something happens to database and it can not be connected.
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
                return True
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return False
    
def create_table(table_name, cursor):
    table = f"""CREATE TABLE IF NOT EXISTS {table_name} (
        Firstname VARCHAR(255),
        Lastname VARCHAR(255),
        Username VARCHAR(255),
        Password VARCHAR(255),
        PC_Score INT,
        User_Score INT
    )"""
    cursor.execute(table)
    print(f"{table_name}Table Created")

def table_exists(table_name):
    #Ensures that table exists
    db = mysql.connector.connect(
        #Since we passed test connection then it is possible to connect. So no need for more testing.
        host='sql11.freesqldatabase.com',
        user='sql11695288',
        password='Q2xne5YcPF',
        database='sql11695288'
    )
    c = db.cursor()
    c.execute('SHOW TABLES LIKE %s', (table_name,))
    
    if c.fetchone() is None:
        create_table(table_name, c)
    else:
        print(f"Table {table_name} Exists")

def add_single_query(table_name, details):
    db = mysql.connector.connect(
        host='sql11.freesqldatabase.com',
        user='sql11695288',
        password='Q2xne5YcPF',
        database='sql11695288'
    )
    c = db.cursor()
    sql = f"INSERT INTO {table_name} (Firstname, Lastname, Username, Password, PC_Score, User_Score) VALUES (%s, %s, %s, %s, %s, %s)"
    c.execute(sql, details)
    
    print('Query added to database succesfully')

    db.commit()
    c.close()
    db.close()

def username_availability(table_name, username):
    try:
        db = mysql.connector.connect(
            host='sql11.freesqldatabase.com',
            user='sql11695288',
            password='Q2xne5YcPF',
            database='sql11695288'
        )
        cursor = db.cursor()

        sql = f"SELECT * FROM {table_name} WHERE Username = %s"
        cursor.execute(sql, (username,))
        
        row = cursor.fetchone()
        
        cursor.close()
        db.close()
        
        print(row)

        if row:
            return False
        else:
            return True
        
    except mysql.connector.Error as e:
        print("Error:", e)
        return True
    

def print_database(): #Mostly For Debugging.
    db = mysql.connector.connect(
        host='sql11.freesqldatabase.com',
        user='sql11695288',
        password='Q2xne5YcPF',
        database='sql11695288'
    )
    cursor = db.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    # Fetch all rows from each table
    for table in tables:
        table_name = table[0]
        print(f"Table: {table_name}")
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    
    cursor.close()
    db.close()

# print_database()