# student_management_system/service.py

from models import Student
from repositories import StudentRepository

class StudentService:
    def __init__(self, repository: StudentRepository):
        self.repo = repository # Dependency injection

    # All methods delegate to repository with validation
    def add_student(self, first_name, last_name, address, nic, nationality, academic_no):
        student = Student(first_name, last_name, address, nic, nationality, academic_no)
        self.repo.add_student(student)

    def search_student(self, academic_no):
        return self.repo.get_student(academic_no)

    def delete_student(self, academic_no):
        self.repo.delete_student(academic_no)

    def update_contact(self, academic_no, address):
        self.repo.update_contact(academic_no, address)

    def view_all_students(self):
        return self.repo.get_all_students()

    def add_subject_marks(self, academic_no, subject, mark):
        student = self.repo.get_student(academic_no)
        if student:
            student.add_subject_mark(subject, mark)

    def view_student_marks(self, academic_no):
        student = self.repo.get_student(academic_no)
        return student.marks if student else None

    def show_average_marks(self, academic_no):
        student = self.repo.get_student(academic_no)
        return student.get_average_marks() if student else None
