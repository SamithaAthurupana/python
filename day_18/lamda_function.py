# ----- Normal function definition -----
def add(a, v):  # define a function named 'add' with two parameters (a, v)
    return a + v  # return the sum of a and v

print(add(3, 5))  # call the function 'add' with arguments 3 and 5 → output: 8

# ----- Using lambda function -----
add_two_num = lambda x, y: x + y  # define an anonymous lambda function and assign it to 'add_two_num'
print(add_two_num(2, 4))  # call the lambda function with arguments 2 and 4 → output: 6

# ----- Immediate lambda execution -----
print((lambda a, b: a * b)(2, 8))  # define and call lambda immediately with arguments (2, 8) → output: 16

# ----- Dictionary of lambda functions -----
math_operation = {
    "Addition": lambda x, y: x + y,       # key 'Addition' maps to lambda that adds two numbers
    "Subtraction": lambda x, y: x - y,   # key 'Subtraction' maps to lambda that subtracts two numbers
}

# loop through dictionary items
for key, value in math_operation.items():
    # key is the string ("Addition"/"Subtraction"), value is the lambda function
    print(f"Operations - {key} | value - {value(10, 20)}")
    # call the lambda with (10, 20) → Addition: 30, Subtraction: -10

# ----- Check even number using lambda -----
print((lambda x: x % 2 == 0)(20))  # returns True if 20 is even

# ----- Map with lambda -----
numbers = [1, 2, 3, 4, 5, 6, 7]  # define a list of numbers

double = list(map(lambda x: x * 2, numbers))  # multiply each number by 2 → return list
print(double)  # output: [2, 4, 6, 8, 10, 12, 14]

# ----- Filter with lambda -----
filter_num = list(filter(lambda x: x % 2, numbers))  # keep only numbers where x % 2 != 0 (odd numbers)
print(filter_num)  # output: [1, 3, 5, 7]
