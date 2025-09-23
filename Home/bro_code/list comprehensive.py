# List comprehension =  A concise way to create list in python
#                       Compact and easier to read than traditional loop
#                       [expression for value in iterable if condition]

'''doubles = []
for x in range(1,11):
    doubles.append(x)

print(doubles)'''

'''doubles = [x * 2 for x in range(1,11)]
triples = [triple * 2 for triple in range(1,11)]
squres = [squre * squre for squre in range(1,11)]

print(squres)
'''
'''fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]

print(fruits)
'''

numbers = [1, -3, 5, -7, 4, 7, 4, 6]
#positive_num = [num for num in numbers if num >= 0]
#negative_num = [num for num in numbers if num <= 0]
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)