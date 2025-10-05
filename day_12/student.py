
class Student:
# now these functions has in the class then we can call these as methods.. because these are in classes.

    def __init__(self):
        print("Constructor called")

    def eat(self):
        print("I'm eating")

    def sleep(self):
        print("I'm Sleeping")


# Creating a object
x = "test"
y = 10
print(type(y))

student1 = Student()
student2 = Student()

print(type(student1))
Student.eat(student1) # we need to add object reference into student.eat parenthesis. because we have called class
student2.eat() # this time we don't need to add object reference into parenthesis.


