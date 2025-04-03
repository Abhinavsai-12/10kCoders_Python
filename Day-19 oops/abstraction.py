from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Class
    @abstractmethod
    def make_sound(self):  # Abstract Method (No implementation)
        pass

class Dog(Animal):  # Concrete Class
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):  # Concrete Class
    def make_sound(self):
        return "Meow! Meow!"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.make_sound())  # ✅ Output: Woof! Woof!
print(cat.make_sound())  # ✅ Output: Meow! Meow!

# animal = Animal()  # Error: Cannot instantiate abstract class