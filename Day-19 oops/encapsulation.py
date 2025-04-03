# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private variable

#     def get_balance(self):  # Getter method to access private variable
#         return self.__balance

#     def deposit(self, amount):  # Public method to modify private variable
#         if amount > 0:
#             self.__balance += amount
#             return f"Deposited {amount}. New balance: {self.__balance}"
#         else:
#             return "Deposit amount must be positive"

# # Creating an object
# account = BankAccount(1000)

# # Accessing private variable using getter method
# print(account.get_balance())  # ✅ Output: 1000

# # Depositing money using public method
# print(account.deposit(500))  # ✅ Output: Deposited 500. New balance: 1500

# # Trying to access private variable directly (❌ Will not work)
# # print(account.__balance)  # ❌ AttributeError: 'BankAccount' object has no attribute '__balance'




# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_age(self):  # Getter method
#         return self.__age

#     def set_age(self, new_age):  # Setter method
#         if new_age > 0:
#             self.__age = new_age
#         else:
#             print("Age must be positive")

# # Creating object
# s1 = Student("Alice", 20)

# print(s1.get_age())  # ✅ Output: 20
# s1.set_age(25)  # ✅ Modifying private variable safely
# print(s1.get_age())  # ✅ Output: 25










class Employee:
    def __init__(self, salary):
        self.__salary = salary  # Private variable

    @property
    def salary(self):  # Getter method
        return self.__salary

    @salary.setter
    def salary(self, amount):  # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Salary must be positive")

# Creating object
e1 = Employee(50000)

print(e1.salary)  # ✅ Output: 50000 (calls the getter method)

e1.salary = 60000  # ✅ Calls the setter method
print(e1.salary)  # ✅ Output: 60000

e1.salary = -1000  # ❌ Output: "Salary must be positive"



















