def add(a,v):
    return a + v
print(add(3,5))

add_two_num = lambda x,y : x + y # giving a name to the anonymous lambda function
print(add_two_num(2,4))
print((lambda a,b:a*b)(2,8)) # writing anonymous functions using lambda

math_operation = {"Addition": lambda x,y:x+y,
                  "Subtraction": lambda x,y: x-y,
                  }

for key, value in math_operation.items():
    print(f"Operations - {key} | value - {value(10,20)}")

print((lambda x: x % 2 == 0)(20))


numbers = [1,2,3,4,5,6,7]
double = list(map(lambda x: x * 2,numbers))
print(double)
filter_num = list(filter(lambda x : x % 2, numbers))
print(filter_num)