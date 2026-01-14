# multilevel inheritance = inherit from a parent which inherits from another parent
#     C(B) <- B(A) <- A

# Grandparent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")


# Parent classes inheriting from Animal
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

# Child class inheriting from Prey and Predator
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# Child class inheriting from two parent classes
class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugss")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()  # Inherited from Animal
rabbit.flee

hawk.eat()  # Inherited from Animal
hawk.hunt()  # Inherited from Predator
# hawk.flee()  # Error: Hawk does not inherit from Prey

# Fish inherits from both Prey and Predator
fish
fish.flee()
fish.hunt()