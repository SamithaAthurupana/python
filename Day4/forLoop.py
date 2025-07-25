import time
'''for i in range(10):
    print(i , end=" ")

print("\n")

for i in range(10, 20):
    print(i , end=" ")

print("\n")

for i in range(0, 100):
    print(i , end=" ")
    if i == 3:
        print("exiting")
        break
    print("hello")
print("exited")

print("\n")

for i in range(0, 100, 10):
    print(i , end=" ")
    if i == 3:
        print("exiting")
        break
    print("hello")
print("exited")

print("\n")'''

'''
#simple countdown 10 - 0
for i in range (10, -1, -1):
    print(i, end=" ")
    time.sleep(1)
'''

#if a number is divisible by 3 print fizz
#if a number is divisible by 5 print buzz
#if a number is divisible by both 3 and 5 print fizzbuzz

for i in range (0, 100):
    if i % 3 == 0 and i % 5 ==0 :
        print(f"Fizzbuzz ")
    elif i % 3 == 0:
        print(f"fizz ")
    elif i % 5 == 0:
        print(f"buzz ")
    else:
        print(i)
