# multiple inheritance = inherit from more than one parent class
#     C(A, B) - > C inherits from A and B

# PARENT CLASSES
class Prey:
    def flee(self):
        print("This animal is fleeing.")

class Predator:
    def hunt(self):
        print("This animal is hunting.")

# CHILD CLASS INHERITING FROM TWO PARENT CLASSES
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# CHILD CLASS INHERITING FROM TWO PARENT CLASSES
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

# Fish inherits from both Prey and Predator
fish.flee()
fish.hunt()