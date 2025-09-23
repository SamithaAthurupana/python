#positional arguments
#Take the first number as a input
#Take the second number as a input
#Take the operator which user want to perform
#then check for the operator with if condition and perform the calculation and print



#print(f"my first name is {first_num}, and my last name is {second_num}")

def multiply(first_num, second_num):
    return first_num * second_num

def addition(first_num, second_num):
    return first_num + second_num

def substraction(first_num, second_num):
    return first_num - second_num

def divide(first_num, second_num):
    return first_num / second_num


def main ():
    first_num = int(input(f"enter the first value: "))
    second_num = int(input(f"enter the second value: "))
    operator = input("Enter operator: ")

    if operator == "+":
        print(first_num + second_num)
    elif operator == "-":
        print(first_num - second_num)
    elif operator == "/":
        if second_num == 0:
            print("wrong number")
        else:
            print(first_num / second_num)
    elif operator == "*":
        print(first_num * second_num)
    else:
        print("wrong operator")
main()