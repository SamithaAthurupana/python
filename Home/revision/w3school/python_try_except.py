# the try block lets you test a block of code for error
# the except block lets you handle the error
# the else block lets you execute code when there is no error
# the finally block lets you execute code, regardless of the try and except blocks

try:
    print(x)
except:
    print("An exception occurred")


try:
    print(y)
except NameError:
    print("Variable x is not define")
except:
    print("An exception occurred")

txt = f"the price is 49 dollars"
print(txt)


