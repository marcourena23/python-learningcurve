# Inheritance = Allows a class to inherit attributes and methods from another class
#                         Helps with code reusability and extensibility
#                         class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        return f"{self.name} is eating."
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
# For a Child class to inherit from a Parent class, we specify the Parent class in parentheses after the Child class name.
class Dog(Animal): # Inheriting from Animal class
    def bark(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal): # Inheriting from Animal class
    def meow(self):
        return f"{self.name} says Meow!"

class Mouse(Animal): # Inheriting from Animal class
    def squeak(self):
        return f"{self.name} says Squeak!"
    
# Example usage:
dog = Dog("Buddy")
print(dog.eat())  # Inherited method from Animal
print(dog.bark()) # Dog's own method
cat = Cat("Whiskers")
print(cat.sleep()) # Inherited method from Animal
print(cat.meow())  # Cat's own method
mouse = Mouse("Mickey")
print(mouse.eat())  # Inherited method from Animal
print(mouse.squeak())  # Mouse's own method