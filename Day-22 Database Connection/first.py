import mysql.connector


connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="py_connection"
)

if connection.is_connected():
    print("connected to mysql")

connection.close()

