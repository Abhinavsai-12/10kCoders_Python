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

    # DELETE all records
    cursor.execute("DELETE FROM students")
    connection.commit()


    print(" Record deleted successfully")


except Error as e:
    print("error at connection ",e)

finally:
    if connection:
        cursor.close()
        connection.close()