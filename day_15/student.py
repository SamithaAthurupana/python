from typing import List
from typeguard import typechecked

@typechecked()
class Student:
    def __init__(self, student_id: str, name: str, age: int, grades: List[int]):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = grades  # must be a list[int]

    def __eq__(self, obj2):  # overriding equal method
        return self.name == obj2.name

    def add_grades(self, grades: List[int]) -> None:
        """Replace the entire grades list with a new list"""
        self.grades = grades

    def add_single_grade(self, grade: int) -> None:
        """Add one grade at a time"""
        self.grades.append(grade)

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


# ---------- Testing ----------
student_obj = Student("223", "eq", 34, [33, 454, 3])

# ✅ Add a single grade
student_obj.add_single_grade(12)

# ✅ Replace grades with a whole new list
student_obj.add_grades([100, 90, 80])

student2 = Student("223", "eq", 34, [33, 454, 3])

if student_obj == student2:
    print("Yes equal")
else:
    print("Not equal")

print("Average:", student_obj.get_average())
