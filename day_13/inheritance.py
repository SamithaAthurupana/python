class Animal:
    def __init__(self, scientific_name, color):
        self.scientific_name = scientific_name
        self.color = color

    def eat(self):
        print(f"{self.scientific_name} is eating")

    def sleep(self):
        print(f"{self.scientific_name} is sleeping")

class Birds(Animal):
    def __init__(self, scientific_name, color, breed):
        Animal.__init__(self, scientific_name, color)
        self.breed = breed

class Mammals(Animal):
    def __init__(self, scientific_name, color, breed):
        Animal.__init__(self, scientific_name, color)
        self.breed = breed

    def drinking_milk(self):
        print(f"{self.scientific_name} with breed {self.breed} is drinking milk.")

class Dog(Mammals):
    def __init__(self, color, breed, tail):
        Mammals.__init__(self,"Canis lupus familiaries", color, breed)
        self.tail = tail


dog = Mammals("Canis lupus familiaries", "black", "bulldog") # instance instantiation
dog.eat() # Canis lupus familiaries is eating

dog = Dog("black", "bulldog", False) # instance instantiation
dog.drinking_milk() # Canis lupus familiaries with breed bulldog is drinking milk.

print(isinstance(dog, Mammals))
print(isinstance(dog, Animal))
print(isinstance(dog, Birds)) # Dog class එක Birds inherit කරන නෑ → False.
print(isinstance(Mammals, Animal))
# 👉 මෙහිදී Mammals කියන්නේ class එක.
# isinstance() function එකෙන් object instances check කරනවා.
# Class එකක් pass කරන නිසා → False.
#
# (ඒ වෙනුවට issubclass(Mammals, Animal) යොදාගත්තොත් → True).
