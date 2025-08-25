

# make a class and get values in to objects.
#   * First we need to make def and instance name and add parameters
#   * Next make a object and assign values after the class name in parentheses.
#   * After that we can call it.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_one = Person("samitha", 23)
print(f"we have a person, his name {person_one.name} and his age is {person_one.age}")
