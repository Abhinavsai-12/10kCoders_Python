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
    #  Update a record
    update_sql = "UPDATE students SET age = %s WHERE name = %s"
    update_val = (23, "Alice")
    cursor.execute(update_sql, update_val)


    connection.commit()
    print(" Record updated successfully")



except Error as e:
    print("error at connection ",e)

finally:
    if connection:
        cursor.close()
        connection.close()