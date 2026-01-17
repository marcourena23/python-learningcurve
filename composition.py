# Composition = The composed object directly own its components, which cannot exist independently
#                "owns-a relationship" --> The whole is composed of the parts

class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        print("Engine started")

class Wheel:
    def __init__(self, size):
        self.size = size

class Car: # composition class 
    def __init__(self, make, model, power, wheel_size):
        self.make = make
        self.model = model
        # Se considera composision  es porque estamos creando objetos de motor y rueda dentro de la clase car
        self.engine = Engine(power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

        def displai_car(self):
            return f"{self.make} {self.model} { self.power}"

car = Car("Ford","Mustang", 500, 18)
