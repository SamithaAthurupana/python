'''for i in range(1,5,2):
    print(i)'''

'''x = "ABCD"
for i in x:
    print(i, end="")'''
# we need to get user input a string and remove vowels and after print it
#1st Method
'''vowels = "aeiou"
result = ""

userInput = input("Enter a word: ").lower()
for i in userInput:
    if i in vowels:
        continue
    else:
        result += i
print("result will be: ",result)'''

#2nd Method
'''userInput = input("enter a word: ").upper()
word_without_vowels = ""
for char in userInput:
    if char == "A":
        continue
    elif char == "E":
        continue
    elif char == "I":
        continue
    elif char == "O":
        continue
    elif char == "U":
        continue
    else:
        word_without_vowels +=char
print("result will be: ",word_without_vowels)
'''

#3rd Method
'''userInput = input("enter a word: ").upper()
word_without_vowels = ""

for char in userInput:
    if char in ['A','E','I','O','U']:
        continue
    else:
        word_without_vowels +=char
print("result will be: ",word_without_vowels)'''

#else block with while loop, always print else not like if else statements
'''i = 1
while i < 5:
    print(i)
    i += 1
else:
    print(i)
print("end")'''
# in the for loop else block excute last vale in if statements
'''i = 1
for i in range(5):
    print(i)
else:
    print("end")
    print(i)'''

'''for i in range(1,2):
    print(i)'''

#range with multiplication table
'''for i in range(1,6):
    print(f"\nMultiplication table for: {i} ")
    for x in range(1,13):
        print(f"{i} * {x} = {i * x}")
    print("========================")'''

x = 6
if not x<5:
    print(x)