items2 = []
for i in range(5):
    items2.append(i+1)
print(items2)

#reverse order print - new items add on 0 index
items2 = []
for i in range(5):
    items2.insert(0, i+1)
print(items2)

#Swap technique withing 2 variable
x = 5
y = 10
print("x = ",x,"y = ",y)

x,y = y,x
print("x = ",x,"y = ",y)

#print string index - Basically string also collection of characters
print("Hello"[2])