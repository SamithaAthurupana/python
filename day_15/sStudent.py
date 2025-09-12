from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    student_id: int
    name: str
    age: int
    grades: List[int]

    def add_grades(self, grades) -> None:
        self.grades = grades

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

student = Student(223, "Test", 23, [13])
print(student)


