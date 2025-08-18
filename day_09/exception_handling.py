'''try:
    user_input = int(input("enter integer: "))
    print(user_input + "hdihbdbdbrbs")

except ValueError:
    print("invalid value as a input..")
except TypeError:
    print("type error")
finally:
    print("Finally block executed..")
'''
'''
try:
    user_input = int(input("enter integer: "))
    print(user_input + "hdihbdbdbrbs")

except (ValueError, TypeError):
    print("value or type error")

finally:
    print("Finally block executed..")
'''

'''try:
    x = int("hello")  # risky: converting text to number
except ValueError:
    print("Oops! That's not a number.")
'''