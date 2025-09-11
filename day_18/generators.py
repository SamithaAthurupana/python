import time
from typing import List



# def generate_numbers(n: int):
#     for i in range(n):
#         yield i
#
# gen = generate_numbers(10)
# print(next(gen))
# print(next(gen))
#
# for i in gen:
#     print(i)
#
#

def generate_numbers():
    yield 10
    yield 11
    yield 12

gen = generate_numbers()
print(next(gen))
print(next(gen))
print(next(gen))

def create_large_list(n):
    return list(range(n))

def create_large_list_yield(n):
    for i in range(n):
        yield i

start_time = time.time()
print(f"List Start Time - {start_time}")
large_list = create_large_list(100000000)
end_time = time.time()
print(f"List end Time - {end_time}")

yield_start_time = time.time()
print(f"End yield Time - {start_time}")
large_list_yield = create_large_list_yield(100000000)
yield_end_time = time.time()
print(f"End yield Time - {end_time}")

def get_even_num(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

def get_even_num_yield(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print(get_even_num(100))

even_num = [i for i in range(100) if i % 2 == 0] #list comprehension
print(even_num)
even_num_gen = (i for i in range(100) if i % 2 == 0) #generator comprehension
print(even_num_gen)