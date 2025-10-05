# student_management_system/repositories.py

from student_management_system.models import Student

class StudentRepository:
    def __init__(self):
        self.students = {}

    def add_student(self, student: Student):
        self.students[student.academic_no] = student

    def get_student(self, academic_no):
        return self.students.get(academic_no)

    def delete_student(self, academic_no):
        if academic_no in self.students:
            del self.students[academic_no]

    def update_contact(self, academic_no, address):
        student = self.get_student(academic_no)
        if student:
            student.address = address

    def get_all_students(self):
        return list(self.students.values())
