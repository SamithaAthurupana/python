from typing import List

class CountDown: # Implement iterate protocol
    def __init__(self, num:int):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        self.num -= 1
        if self.num == 0:
            raise StopIteration
        return self.num

count_down = CountDown(10)# Create an iterator then calls the next method in the iterator object
print(count_down)

count_down = CountDown(10)
count_down_iter = iter(count_down)

print(count_down_iter.__next__())
print(count_down_iter.__next__())
print(count_down_iter.__next__())
print("==============")
for i in count_down:
    print(i)
print("-------------------------------------------------------")

def generate_numbers(n: int) ->List[int]:
    result = []

    for i in range(n):
        result.append(i)
    return result

print(generate_numbers(10))
for num in generate_numbers(10):
    print(num)

print("-------------------------------------------------------")

