import time
from dataclasses import dataclass

def fun_a():
    yield 10
    print("hello")
    yield 20

def main():
    obj = fun_a()
    print(next(obj))
    print(next(obj))


main()