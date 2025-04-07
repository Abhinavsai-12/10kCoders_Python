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

    # cursor.execute("select * from students")
    # print(cursor.fetchall())


    cursor.execute("select * from students")
    result=cursor.fetchall()

    for row in result:
        print(row)
    

except Error as e:
    print("error at connection ",e)

finally:
    if connection:
        cursor.close()
        connection.close()