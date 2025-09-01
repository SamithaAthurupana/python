# inheritance = Allows a class to inherite attributes and methods from another class
#               Help with code reusability and extensibility
#               class Child(parent)




class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} are eating!")

    def sleep(self):
        print(f"{self.name} are eating!")

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.speak()
