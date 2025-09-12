try:
    x = int(input("Enter digits: "))
except Exception as e:
    print(e)

try:
    x = int(input("Enter digits: "))
except BaseException as e:
    print(e)

try:
    x = int(input("Enter digits: "))
except ValueError as e:
    print(e)

#when we handle exceptions, we need to handle most specific exceptions

'''try:
    x = int(input("Enter digits: "))
except (ValueError,ZeroDivisionError):
    print("Test")

text = "x"
try:
    while True:
        text = text + text
        print(len(text))
except MemoryError:
    print("out of memory")'''