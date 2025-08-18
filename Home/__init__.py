'''print(2+2)
print(50-5*6)
print((50-5*6)/4)
print(8/5)

#division always return float, we can get integer result using floor division
print(17/3) #5.666666666666667
print(17//3) #5 (floor division)
print(17%3) #2 reminder of the division

#with python, it is possible to use the ** operator to calculate powers
print(5**2) #5 squared = 25

width = 20
height = 5 * 9
print(width * height) #900'''
'''
#swap using variable 3
a = 25
b = 34
temp = 0

temp += a
a -= temp
a += b
b -= b
b += temp
temp -= b

print("a = ", a,"b = ", b,"temp = ", temp)'''
'''
#swap using 2 variable
a = 5
b = 10

print("Before swap: a =", a, ", b =", b)'''

# Swap directly
'''(a, b) = (b, a)'''

'''print("After swap: a =", a, ", b =", b)'''

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals)
print(capitals.get("USA"))
capitals.update({"Germany":"Berlin"})
print(capitals)

keys = capitals.keys()
print(keys)

for i in capitals.keys():
    print(i, end=", ")
print()

items = capitals.items()
print(items,"\n")

for key, value in capitals.items():
    print(f"{key}: {value}")




























