from car import Car

car1 = Car("Mustang", 2024, "Red", False)

print(f"Model: {car1.model}")
print(f"Year: {car1.year}")
print(f"Color: {car1.color}")
print(f"For Sale: {car1.for_sale}")

print("--------------------------------")
car1.drive()
car1
