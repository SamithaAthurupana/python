# class variable = shared among all instance of class
#                   Define outside the constructor
#                   Allow you to share data among all objects created from that class


class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("sponchbob", 30)
student2 = Student("spongee", 33)

print(student1.name)
print(student1.class_year)
print(f"my class has {Student.num_students} students")