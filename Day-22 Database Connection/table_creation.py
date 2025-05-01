import mysql.connector
from mysql.connector import Error

try:
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="py_connection"
    )

    if connection.is_connected():
        print("connected to mysql")


    cursor = connection.cursor()

    # cursor.execute("SHOW DATABASES")  # Show all databases
    # for db in cursor:
    #     print(db)




    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student1 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
    """)

    connection.commit()




except Error as e:
    print("error at connection ",e)


finally:
    if connection:
        cursor.close()
        connection.close()
