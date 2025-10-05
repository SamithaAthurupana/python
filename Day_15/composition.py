
from typing import List
# concept එක Composition (අපේ class එකක් ඇතුළේ වෙන class එකක් object එකක් විදිහට use කරන එක
class Engine:
    def __init__(self, horsepower: int, capacity: str):
        self.horsepower = horsepower
        self.capacity = capacity

    def start(self) -> None:
        print("Engine Started")


class Car:
    def __init__(self, model: str, engine: Engine):
        self.model = model
        self.engine = engine

    def print_car_info(self) -> None:
        print(f"Car Model - {self.model} - car has a Engine - {self.engine.capacity}")

    def start(self) -> None:
        print(f"Starting the car {self.model} ...")
        self.engine.start()   # calling Engine class method


# create car with engine
car = Car("Toyota", Engine(1000, "2500CC"))

car.print_car_info()   # print car + engine info
car.engine.start()     # directly call engine start
car.start()        # start car → internally starts engine
