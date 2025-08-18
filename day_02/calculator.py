#Take the first number as a input
#Take the second number as a input
#Take the operator which user want to perform
#then check for the operator with if condition and perform the calculation and print

numberOne = int(input("Enter first number: "))
operator = (input("Enter operator: "))
numberTwo = int(input("Enter Second number: "))

if operator == "+":
    print(numberOne + numberTwo)
elif operator == "-":
    print(numberOne - numberTwo)
elif operator == "/":
    if numberTwo == 0:
        print("wrong number")
    else:
        print(numberOne / numberTwo)
elif operator == "*":
    print(numberOne * numberTwo)
else:
    print("wrong operator")