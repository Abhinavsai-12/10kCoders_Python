# # Define a class
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def display_info(self):
#         print(f"Car: {self.brand} {self.model}")

# # Creating an object of the class
# car1 = Car("Toyota", "Corolla")
# car1.display_info()









# class car:
#     wheels=4

#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# car1=car("Tayota","corolla")
# car1=car("Hpnda","Civic")

# print(car1.wheels)
# print(car1.brand)
# print(car1.model)




# class Car:
#     wheels = 4  # Class variable

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     @classmethod
#     def change_wheels(cls, new_wheels):
#         cls.wheels = new_wheels  # Modifying class attribute

#     @classmethod
#     def show_wheels(cls):
#         print(f"All cars have {cls.wheels} wheels")

# # Using class method without creating an object
# Car.change_wheels(6)  # Changing class attribute
# Car.show_wheels()  # Output: All cars have 6 wheels
# print(Car.wheels)






class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods without creating an object
print(MathOperations.add(5, 10))        # Output: 15
print(MathOperations.multiply(4, 6))    # Output: 24


