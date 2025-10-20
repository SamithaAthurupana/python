# print((40/64)*100)
'''
count = 0
x = ["cat", "dog", "test", "dad", "cat", "test"]

b = {value == "cat" for value in x}

print(b)'''

# user input words, append, when it stop write for loop and next iterate each words and make dictionary,
# dictionary value =  word and make index into key value,
# identify how many words are == to cat

'''
animals = []
user_input = 0
frequency_count = {}

while True:
    if user_input == "q":
        break
    else:
        user_input = input("Enter animal name: ").lower().strip()
        animals.append(user_input)

animals.pop()
print(animals)'''

# second method using dictionary
'''
for animal in animals:
    if animal in frequency_count.keys():
        frequency_count[animal] += 1
    else:
        frequency_count[animal] = 1
print(frequency_count)'''

#first Method with for and if
'''
count = 0
for animal in animals:
    if animal == "cat":
        count +=1
print(f"cat count is: {count}")'''
#
# print([1,2,3][1:3])


# animal = []
#
# while True:
#     user_in = input("Enter animal name: ").lower().strip()
#     if user_in == "q":
#         break
#     else:
#         animal.append(user_in)
# print(animal)
