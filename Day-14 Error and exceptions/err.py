# n=13
# try:
#     result=n/0
# except:
#     print("Cannot divide with zero")





# finally block
try:
    f = open("file.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("Error: File not found!")
except:
    print("file is found")
finally:
    print("Execution completed.")



