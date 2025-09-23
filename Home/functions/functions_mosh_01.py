#parameters - input that you add in functions
#argument - actual value given parameters
# Functions are,
#               1. perform a task
#               2. Return a value

'''def greet():
    print("Hi there")
    print("Hi there")


greet()'''
'''
def hello(first_name, age):
    print(f"hello {first_name},")
    print(f"you are {age} years old.")


hello("samitha", 27 )'''

'''def get_greet(name):
    return f"Hi {name}"

get_greet("samitha")
print(get_greet("samitha"))'''
'''
# keyword arguments
def increment(number, by):
    return number + by

print(increment(2,by=1))
# in here by is the keyword argument - it helps more readble..
'''
'''def increment(number, by=1):
    return number + by

print(increment(2))
# we can use by as optional argument
'''
'''
#arg
# with parameters having * - final code will be tupple
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2,3,4,5))

#**args
def save_user(**user):
    print(user)
    print(user["name"])

save_user(id=1, name="john", age=22)

#scope
message = "a"
def greet(name):
    global message
    message = "b"

greet("mosh")
print(message)'''
'''
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input

print(fizz_buzz(15))'''

'''def els(num,num2):
    total = num * num2
    return total

print(els(3,2))'''

#===========================================================


