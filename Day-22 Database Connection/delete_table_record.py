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

    # DELETE a record where name is 'John'
    delete_sql = "DELETE FROM students WHERE name = %s"
    delete_val = ("John",)
    cursor.execute(delete_sql, delete_val)


    connection.commit()
    print(" Record deleted successfully")


except Error as e:
    print("error at connection ",e)

finally:
    if connection:
        cursor.close()
        connection.close()