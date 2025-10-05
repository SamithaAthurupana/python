class Rectangle:
    def __init__(self):
        self.length = 20
        self.width = 30

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return self.width + self.length

rect = Rectangle()
area1 = rect.area()
print(f"area: {area1}")

perimeter_of_rectangle = rect.perimeter()
print(f"perimeter: {perimeter_of_rectangle}")
