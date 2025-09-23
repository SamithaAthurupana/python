'''#print(4 & 5)
print(4 | 5)
#compliment ~
print(~12)
#xor bitwise exclusive
print(10 ^ 13)
print(5<<2)
print(5>>2)
'''
user_number = int(input("Enter number: "))

#print(user_number & 1)

if user_number & 1:
    print("Number is odd")
else:
    print("Number is even")