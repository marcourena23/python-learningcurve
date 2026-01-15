# Polymorphism = Many forms of the same function
#                 The same function name can be used for different classes
#                 Allows objects of different classes to be treated as objects of a common superclass
#                 "Un mismo método puede comportarse de manera diferente según el objeto que lo llame"

# El polimorfismo es uno de los pilares de la programación orientada a objetos.
# Permite que diferentes clases implementen el mismo método de manera diferente,
# pero puedan ser tratadas de forma uniforme a través de una interfaz común.

# Ejemplo 1: Polimorfismo con métodos con el mismo nombre

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):  # Método que será sobrescrito (polimórfico)
        return f"{self.name} makes a sound."

class Dog(Animal):
    def make_sound(self):  # Implementación específica para Dog
        return f"{self.name} says Woof! Woof!"

class Cat(Animal):
    def make_sound(self):  # Implementación específica para Cat
        return f"{self.name} says Meow! Meow!"

class Duck(Animal):
    def make_sound(self):  # Implementación específica para Duck
        return f"{self.name} says Quack! Quack!"

# Ejemplo de uso del polimorfismo
print("=== Ejemplo 1: Polimorfismo básico ===")
dog = Dog("Buddy")
cat = Cat("Whiskers")
duck = Duck("Donald")

# Todos los animales tienen el método make_sound(), pero cada uno se comporta diferente
print(dog.make_sound())
print(cat.make_sound())
print(duck.make_sound())

print("\n=== Ejemplo 2: Polimorfismo con una función común ===")
# Podemos tratar diferentes objetos de manera uniforme
def animal_speak(animal):  # Esta función acepta cualquier Animal
    print(animal.make_sound())  # No importa qué tipo de animal sea

# Llamamos la misma función con diferentes tipos de animales
animal_speak(dog)
animal_speak(cat)
animal_speak(duck)

print("\n=== Ejemplo 3: Polimorfismo con listas ===")
# Podemos almacenar diferentes tipos en una lista y tratarlos uniformemente
animals = [Dog("Max"), Cat("Luna"), Duck("Daisy")]

for animal in animals:
    print(animal.make_sound())  # Cada animal ejecuta su propia versión del método

print("\n=== Ejemplo 4: Polimorfismo con formas geométricas ===")

class Shape:
    def __init__(self, name):
        self.name = name
    
    def calculate_area(self):  # Método polimórfico
        pass  # Será implementado por las clases hijas

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return (self.base * self.height) / 2

# Crear diferentes formas
rectangle = Rectangle("Rectángulo", 5, 10)
circle = Circle("Círculo", 7)
triangle = Triangle("Triángulo", 6, 8)

# Todas las formas tienen calculate_area(), pero cada una calcula diferente
shapes = [rectangle, circle, triangle]

for shape in shapes:
    area = shape.calculate_area()
    print(f"El área de {shape.name} es: {area:.2f}")

print("\n=== Ventajas del Polimorfismo ===")
print("1. Flexibilidad: Puedes agregar nuevas clases sin modificar el código existente")
print("2. Código más limpio: No necesitas verificar el tipo de objeto antes de llamar métodos")
print("3. Extensibilidad: Fácil agregar nuevos comportamientos")
print("4. Mantenibilidad: Código más organizado y fácil de mantener")