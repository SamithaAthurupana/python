kiloMeters=2
kiloMeters = kiloMeters + 1
kiloMeters += 1
print("Km to Meters =", kiloMeters * 1000)

i = 10
j = 20
#Increase the value of i by 2 and then multiply by j
i += 2 * j
print("Answer = ", i )

#
x = 10
y = 20
z = 15

var = 100
#Add x,y,z and reduce it from var variable
print("Answer = " ,var-(x+y+z)) # What is the expected thing using normal arithmatic
var -= (x+y+z)
print("Answer = ",var) #real answers

#Swap the values without third variable
a = 20
b = 30
print("a = ", a, "b",b) # Real answers

a = a + b #a becomes 50 (20 + 30 = 50)                      Another Operation a+=b
b = a - b #b becomes 20 (50 - 30 = 20) {Original a}         Another Operation a -= b
a = a - b #a become 30 (50 - 20 = 30) {Original b}          Another Operation a -= b
print("a = ", a, "b",b) # Answers after swap
