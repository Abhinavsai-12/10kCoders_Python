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


    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("John", 20))



    sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
    val = ("Alice", 22)
    cursor.execute(sql,val)

    connection.commit()
    print("Data entered")




except Error as e:
    print("error at connection ",e)


finally:
    if connection:
        cursor.close()
        connection.close()
