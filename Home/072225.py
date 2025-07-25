'''a = [ "banana", "apple", "microsoft"]
print(a[0])
print(a[1])
print(a[2]

for element in a:
    print(element)'''

'''b = [20, 10, 5]
total = 0
for e in b:
    total = total + e
    print(total)'''

'''c = list(range(1,5))
total12 = 0
for i in range(1,5):
    total12 += i
print(total12)'''

'''print(list(range(1,100)))'''

#while loop = execute some code While some condition remains true
'''name = input("Enter Your Name: ")
if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}")'''

'''name = input("Enter Your Name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter Your Name: ")
print(f"Hello {name}")'''

'''age = int(input("Enter your age: "))
while age < 0 :
    print("Age can not be negative..")
    age = int(input("Enter your age: "))
print(f"you are {age} years old")'''

'''food = input("Enter any food you like ( quite enter q): ")
while not food == "q":
    print(f"food name: {food}")
    food = input("Enter any food you like ( quite enter q): ")
print("bye")'''

'''num = int(input("Enter number between 1 - 10: "))
while num < 0 or num > 10:
    print("Wrong number..")
    num = int(input("Enter number between 1 - 10: "))
print(f"Your Entered number is: {num}")'''

'''nums = [1,45,22,4]
for num in nums:
    print(num)'''

'''nums = [1,45,22,4,55]
for num in nums:
    if num == 4:
        print(f"we found: {num}")
        continue
    print(num)'''

'''nums = [1,2,3,4,5]
for num in nums:
    for letters in 'abc':
        print(num, letters)'''

'''for i in range(1, 11):
    print(i)'''

'''x = 0
while x < 10:
    print(x)
    x += 1'''

'''x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1'''

'''print(range (5))
print(list(range(5)))

a = ['may', 'susi', 'mala']
print(a)
for i in range(len(a)):
    print(i, a[i])'''

#nexted loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

'''for x in range(1, 10):
    print(x, end=" ")'''

'''for y in range(3):
    for x in range(1, 10):
        print(x, end=" ")
    print()'''

rows = int(input("Enter the Number of rows: "))
columns = int(input("Enter the Number of Columns: "))
symbols = input("Enter the symbol: ")

for x in range (rows):
    for y in range(columns):
        print(symbols, end="")
    print()