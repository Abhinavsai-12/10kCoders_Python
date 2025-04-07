# First, open MySQL and run:

# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(100) UNIQUE NOT NULL,
#     password VARCHAR(255) NOT NULL
# );


import mysql.connector
from mysql.connector import Error



try:
    # Connect to database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="py_connection"

    )




    cursor = mydb.cursor()

    # Signup function
    def signup():
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            mydb.commit()
            print("✅ Signup successful!")
        except mysql.connector.IntegrityError:
            print("❗ Username already exists. Try a different one.")

    # Login function
    def login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()

        if result:
            print("🔓 Login successful! Welcome,", username)
        else:
            print("❌ Invalid credentials. Try again.")

    # Menu
    while True:
        print("\n===== Login/Signup System =====")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")



except Error as e:
    print("error at connection ",e)

finally:
    if mydb:
        cursor.close()
        mydb.close()