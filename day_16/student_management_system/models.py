# student_management_system/models.py

class Student:
    def __init__(self, first_name, last_name, address, nic, nationality, academic_no):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.nic = nic
        self.nationality = nationality
        self.academic_no = academic_no
        self.marks = {}

    def add_subject_mark(self, subject, mark):
        self.marks[subject] = mark

    def get_average_marks(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

