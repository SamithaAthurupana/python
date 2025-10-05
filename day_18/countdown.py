from typing import List  # Import List type hinting for Python type annotations

class CountDown:  # A class implementing the iterator protocol
    def __init__(self, num: int):  # constructor takes a number as input
        self.num = num  # initialize instance variable 'num'

    def __iter__(self):  # define __iter__ method to make this class iterable
        return self  # return the object itself (iterator is also the iterable)

    def __next__(self):  # define __next__ method which gives the next value in iteration
        self.num -= 1  # reduce number by 1 on each call
        if self.num == 0:  # stop condition (when num becomes 0)
            raise StopIteration  # signal that iteration is finished
        return self.num  # otherwise return the current value

count_down = CountDown(10)  # create an iterator with starting number 10
print(count_down)  # printing object (will show memory location, not values)

count_down = CountDown(10)  # create new countdown object
count_down_iter = iter(count_down)  # get iterator by calling iter()

print(count_down_iter.__next__())  # call next → returns 9
print(count_down_iter.__next__())  # call next → returns 8
print(count_down_iter.__next__())  # call next → returns 7

print("==============")
for i in count_down:  # for loop uses iterator protocol internally
    print(i)  # keeps calling __next__ until StopIteration is raised

print("-------------------------------------------------------")
print("-------------------------------------------------------")

def generate_numbers(n: int) -> List[int]:  # function returning list of numbers
    result = []  # empty list
    for i in range(n):  # loop from 0 to n-1
        result.append(i)  # append each number to result list
    return result  # return the final list

print(generate_numbers(10))  # prints full list [0,1,2,3,4,5,6,7,8,9]

for num in generate_numbers(10):  # iterate through the list
    print(num)  # print each number separately

