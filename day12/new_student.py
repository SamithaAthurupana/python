class NewStudent:
# now these functions has in the class then we can call these as methods.. because these are in classes.

    def __init__(self,name, age, institute):
        self.name = name
        self.age = age
        self.institute = institute
        print("Constructor called")

    def eat(self):
        print(f"I'm eating {self.name} {self.age}")

    def sleep(self):
        print("I'm Sleeping")

    def show_details(self):
        print(f"Name - {self.name} Age - {self.age} campus - {self.institute}")

    def compare(self,std):
        return self.name == std.name


'''student1 = NewStudent("samitha", 23)
student2 = NewStudent("waruna", 32)

NewStudent.eat(student2)
NewStudent.eat(student1)
'''
student1 = NewStudent("samitha", 27, "KDU")
student2 = NewStudent("samitha", 27,"KDU")

NewStudent.show_details(student1)

print(student2 == student1)
# print False because addresses are note same
print(student2)
print(student1)

if student1.compare(student2):
    print("values are same")