#take 2 numbers as a input and check the largest number
#if number one is grater than number two, check whether the number is even or odd
numberOne = int(input("Enter your Number one:"))
numberTwo= int(input("Enter your Number Two:"))

if numberOne > numberTwo:
    print(f"Number one is Largest Number: {numberTwo}")
    if numberTwo % 2 == 0:
        print("even number")
        if numberTwo % 4 == 0:
            print(f"Divisible by 4, {numberTwo}")
        else:
            print(f"Not Divisible by 4, {numberTwo}")
    else:
        print("odd number")
elif numberTwo > numberOne:
    print(f"Number Two is Largest Number: {numberOne}")
    if numberOne % 2 == 0:
        print("even number")
        if numberOne % 4 == 0:
            print(f"Divisible by 4, {numberOne}")
        else:
            print(f"Not Divisible by 4, {numberOne}")
    else:
        print("odd number")

else:
    print(f"Both numbers are equal, {numberOne},{numberTwo}")


