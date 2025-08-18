'''#build in functions
a = abs(-10.4)
print(a)
'''
'''def func():
    print("hllo")


func()'''

'''def func1():
    name= input("enter your name: ")
    print(f"your name is {name}")


func1()'''
'''
def ft_to_cm(ft):
    centimeter = ft * 30.48
    return centimeter

print(ft_to_cm(320))'''

'''def add(a,b):
    sum_of_val = a + b
    print(sum_of_val)

add(4,7)'''

'''def absolute(x):
    if x >= 0:
        return x
    else:
        return -x


print(absolute(4))'''

'''def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(6))
'''

'''#default arg
def welcom(name = "paul"):
    print("hello", name)

welcom()
welcom("samitha")'''

'''def message(name1, name2, name3):
    print("hello", name1, "please tell ", name2, "that ", name3, "is waiting")

message("samitha", "gilly", "showa")'''

def welcome(*names):
    print("hello", names[0],", ",names[1])

welcome("shashika","wasantha")

