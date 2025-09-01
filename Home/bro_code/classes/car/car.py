
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive a car {self.model}")

    def stop(self):
        print(f"you stopped car {self.model}")

    def describe(self):
        print(f"your car is {self.model} - {self.year} - {self.color} - is it sale:{self.for_sale}")