import time
from dataclasses import dataclass


@dataclass
class Student:
    age:int

def fun_b():
    print("function B")

def fun_a():
    time.sleep(10)
    fun_b()
    print("function A")

def main():#syncronous
    fun_a()
    student = Student(20)
    print("Hello")


main()