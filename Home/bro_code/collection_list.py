#collection = single variable used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   set = {} unordered list immutable, but Add/remove OK. No duplication
#   Tuple = () ordered and unchangeable. Duplicates OK. Faster

fruits =["apple", "orange", "banana", "coconut"]
print(fruits)
print(fruits[2])
print(fruits[0:3])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])

for x in fruits:
    print(x)

print(len(fruits))
print("apple" in fruits)

fruits [0] = "removed"
print(fruits)

fruits.append("pineapple")
fruits.insert(0,"Abb")
for i in fruits:
    print(i)


