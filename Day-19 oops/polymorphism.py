# class Animal:
#     def make_sound(self):
#         print("Animal makes a sound.")

# class Dog(Animal):
#     def make_sound(self):  # Overriding parent method
#         print("Dog barks.")

# class Cat(Animal):
#     def make_sound(self):  # Overriding parent method
#         print("Cat meows.")

# # Creating objects
# animals = [Dog(), Cat(), Animal()]

# # Using polymorphism
# for animal in animals:
#     animal.make_sound()




# # #overloading
# class MathOperations:
#     def add(self, a, b=0, c=0):
#         return a + b + c

# math = MathOperations()
# print(math.add(5))       # Output: 5
# print(math.add(5, 10))   # Output: 15
# print(math.add(5, 10, 20)) # Output: 35





# #operator overloading

# class Book:
#     def __init__(self, pages):
#         self.pages = pages

#     def __add__(self, other):  # Overloading +
#         return Book(self.pages + other.pages)

#     def __str__(self):
#         return f"Total pages: {self.pages}"

# book1 = Book(100)
# book2 = Book(200)
# book3 = book1 + book2  # Uses __add__()

# print(book3)  # Output: Total pages: 300




# # 4. Polymorphism with Functions and Classes
# class Circle:
#     def area(self, radius):
#         return 3.14 * radius * radius

# class Square:
#     def area(self, side):
#         return side * side

# # Function using polymorphism
# def print_area(shape, value):
#     print(f"Area: {shape.area(value)}")

# # Creating objects
# circle = Circle()
# square = Square()

# # Calling function with different objects
# print_area(circle, 5)  # Output: Area: 78.5
# print_area(square, 4)  # Output: Area: 16
