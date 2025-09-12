from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    def calculate_area(self) -> float:
        return self.length * self.width


# Test individual objects
circ_obj = Circle(23)
print(circ_obj.calculate_area())  # 1661.06

rec_obj = Rectangle(12, 45)
print(rec_obj.calculate_area())   # 540


# List of shapes
shapes: List[Shape] = [Circle(10), Rectangle(70, 34)]

for shape in shapes:
    print(shape.calculate_area())  # 314.0 , 2380
