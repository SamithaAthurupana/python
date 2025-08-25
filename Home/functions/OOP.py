# OOP stands for Object-Oriented Programming.
# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
#
# Advantages of OOP
#   * Provides a clear structure to programs
#   * Makes code easier to maintain, reuse, and debug
#   * Helps keep your code DRY (Don't Repeat Yourself)
#
#  Class	Objects
#  Fruit	Apple, Banana, Mango
#  Car	    Volvo, Audi, Toyota
#
# Python Classes/Objects
#   * Python is an object oriented programming language.
#   * Almost everything in Python is an object, with its properties and methods.
#   * A Class is like an object constructor, or a "blueprint" for creating objects.
#
# Create a Class
# class MyClass:
#   x = 5
#
# call object in class -------------- as we call append in list
# class MyClass:
#   x = 5
# print(MyClass.x)
#
# Create Object
# Now we can use the class named MyClass to create objects:
# Create an object named p1, and print the value of x:
# p1 = MyClass()
# print(p1.x)
#
# make a class and get values in to objects.
#   * First we need to make def and instance name and add parameters
#   * Next make a object and assign values after the class name in parentheses.
#   * After that we can call it.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person_one = Person("samitha", 23)
# print(f"we have a person, his name {person_one.name} and his age is {person_one.age}")

# __init__() කියන්නේ මොකක්ද?
# __init__() කියන්නේ Python classes වල constructor method එක.
# Object එකක් නවතෙන් සාදාගන්න විට (new object create කරන විට) automatic ලෙස කැඳවෙන method එක.
# මේකෙ primary භූමිකාව තමයි object එක initialize කිරීම (object එකේ attribute වලට values දාගැනීම).

# 🔹 වැදගත් කරුණු
# __init__() constructor → object එක create වෙන වෙලාවේ run වෙනවා.
# self කියන්නේ object එකේම reference (object එක තුල attribute එකක් access කරන්න).
# Class එකේදී object එකේ attributes (දත්ත) initialize කරන්න මෙය mostly භාවිතා වෙනවා.

# class Person:
#     def __init__(self, name, age):
#         # මේකෙන් object එකේ attributes initialize කරනවා
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} ගේ වයස {self.age}යි."
#
# # නව object එකක් create කරන විට __init__() auto run වෙනවා
# p1 = Person("අනුෂා", 22)
# p2 = Person("දිනූෂා", 30)
#
# print(p1)
# print(p2)

# __str__() කියන්නේ මොකක්ද?
# Python එකේ special method (dunder method) එකක්.
# print() function එක හෝ str() function එකකින් object එක print කරන විට, අයෙකුට කියවන්න ලේසියෙන් පෙනෙන string එකක් ලබා දේ.
# __str__() method එකක් define කරලා නැත්නම්, Python එක object එක print කරද්දී මෙහෙම අකුරු පෙන්වයි:
# <__main__.ClassName object at 0x000001A23B4C>

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # __str__() define කරලා
#     def __str__(self):
#         return f"{self.name} ගේ වයස {self.age}යි."
#
# p1 = Person("කවින්", 25)
#
# print(p1)  # __str__() tự动 ලෙස කැඳවයි
# print(str(p1))  # str() function එකෙන් හෝ කැඳවන්න පුළුවන්

# Object creating
class Person:
  def __init__(self, name, age):            # constructor (object එක හදുമ്പോලම ක්‍රියාත්මක වෙන විශේෂ method එක)
    self.name = name                        # object එකේ (instance එකේ) name කියන ගුණාංගය සකස් කරනවා
    self.age = age                          # object එකේ age ගුණාංගය සකස් කරනවා

  def myfunc(self):                         # class එක තුළ ඇති method එකක්
    print("Hello my name is " + self.name)  # self.name වල තියෙන අගය ප්‍රින්ට් කරනවා

p1 = Person("John", 36)          # Person class එකෙන් p1 කියන object එකක් සාදනවා
p1.myfunc()                                 # p1 object එකේ myfunc() method එක කැඳවනවා

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()  # Output: Hello my name is John

# Modify Object Properties ------------
# You can modify properties on objects like this:
# Example
# Set the age of p1 to 40:
# p1.age = 40

# Modify Object Properties ------------
# You can modify properties on objects like this:
# Example
# Set the age of p1 to 40:
# p1.age = 40

# Delete Objects
# You can delete objects by using the del keyword:
# Example
# Delete the p1 object:
# del p1

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
# Example
# class Person:
#   pass

# Inheritance ------------------------
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

# මෙම කේතයෙන් කරන්නේ Person class එකෙන් උරුම කරගන්නා (inherit) Student class එකක් සාදලා, super() භාවිතයෙන් parent class එකේ init කැඳවා attributes සැමරිතින ලෙස සකස් කිරීමයි.
# කේතයේ ක්‍රියාවලිය:
# Person:
# init(self, fname, lname): firstname සහ lastname set කරනවා.
# printname(self): නාමය print කරන method එක.
# Student(Person):
# Person එකෙන් උරුම වෙනවා.
# init(self, fname, lname):
# super().init(fname, lname) කියලා parent (Person) එකේ init කැඳවලා firstname/lastname set කරගන්නවා.
# self.graduationyear = 2019 කියලා අමතර attribute එකක් දාන්නා.
# ධාවකය:
#
# x = Student("Mike", "Olsen")
# print(x.graduationyear) → 2019
# අමතරව, Student object එකට Person එකේ method එකත් තිබෙන නිසා: