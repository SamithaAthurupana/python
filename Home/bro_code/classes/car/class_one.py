# object = A "bundle of related attributes (variables) and methods (functions)
#           Ex: phone, cup, book
#           You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Mustang", 2024,"red",False)
print(car1)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()
car1.describe()