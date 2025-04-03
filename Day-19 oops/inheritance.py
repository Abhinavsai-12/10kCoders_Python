# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print("Animal makes Sound")

#     def info(self):
#         print("This is an animal")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks")

# dog=Dog("buddy")
# dog.speak()
# dog.info()




# # Multiple inheritance
# # Parent class 1
# class Father:
#     def personality(self):
#         print("Father is disciplined.")

# # Parent class 2
# class Mother:
#     def nature(self):
#         print("Mother is caring.")

# # Child class inheriting from both
# class Child(Father, Mother):
#     def show_traits(self):
#         self.personality()  # Inherited from Father
#         self.nature()       # Inherited from Mother

# # Creating object
# child = Child()
# child.show_traits()
# # Output:
# # Father is disciplined.
# # Mother is caring.






# # #multi level inheritance
# # Grandparent class
# class Grandparent:
#     def show_grandparent(self):
#         print("I am the grandparent.")

# # Parent class inheriting from Grandparent
# class Parent(Grandparent):
#     def show_parent(self):
#         print("I am the parent.")

# # Child class inheriting from Parent
# class Child(Parent):
#     def show_child(self):
#         print("I am the child.")

# # Creating an object of Child
# child = Child()
# child.show_grandparent()  # Output: I am the grandparent.
# child.show_parent()       # Output: I am the parent.
# child.show_child()        # Output: I am the child.



# #Hierarchical inheritance

# # Parent class
# class Vehicle:
#     def general_info(self):
#         print("Vehicles are used for transportation.")

# # Child class 1
# class Car(Vehicle):
#     def car_info(self):
#         print("Cars have four wheels.")

# # Child class 2
# class Bike(Vehicle):
#     def bike_info(self):
#         print("Bikes have two wheels.")

# # Creating objects
# car = Car()
# car.general_info()  # Output: Vehicles are used for transportation.
# car.car_info()      # Output: Cars have four wheels.

# bike = Bike()
# bike.general_info()  # Output: Vehicles are used for transportation.
# bike.bike_info()     # Output: Bikes have two wheels.






# #Hybrid inheritance
# # Parent class
# class Engine:
#     def engine_info(self):
#         print("Engine is essential for a vehicle.")

# # Parent class 2
# class Vehicle:
#     def vehicle_info(self):
#         print("A vehicle is used for transportation.")

# # Intermediate class (inherits from Engine and Vehicle)
# class Car(Engine, Vehicle):
#     def car_info(self):
#         print("Cars usually have 4 wheels.")

# # Final subclass
# class SportsCar(Car):
#     def sports_car_info(self):
#         print("Sports cars are fast.")

# # Creating an object of SportsCar
# sports_car = SportsCar()
# sports_car.engine_info()     # Output: Engine is essential for a vehicle.
# sports_car.vehicle_info()    # Output: A vehicle is used for transportation.
# sports_car.car_info()        # Output: Cars usually have 4 wheels.
# sports_car.sports_car_info() # Output: Sports cars are fast.




# # Method Overriding in Inheritance

# class Parent:
#     def show_message(self):
#         print("This is the parent class.")

# class Child(Parent):
#     def show_message(self):  # Overriding parent method
#         print("This is the child class.")

# child = Child()
# child.show_message()  # Output: This is the child class.





# # Using super() in Inheritance
# # The super() function is used to call a method from the parent class inside the child class.

# class Parent:
#     def show_message(self):
#         print("This is the parent class.")

# class Child(Parent):
#     def show_message(self):
#         super().show_message()  # Call parent method
#         print("This is the child class.")

# child = Child()
# child.show_message()
# # Output:
# # This is the parent class.
# # This is the child class.




