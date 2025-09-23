'''print("------in normal list with one for loop-------------------")
abc = ["A","B","C"]

for alp in abc:
    print(alp)'''

groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"], ["chicken", "fish", "turkey"]]

'''
print("------in normal list with one for loop-------------------")
for collection in groceries:
    print(collection)'''

'''#variable දෙකක් වෙන්න ඕන. main එකේ variable එක යටට යන්න ඕන
for collection in groceries:
    for food in collection:
        print(food)
'''
'''for collection in groceries:
    for food in collection:
        print(food, end =" ")
    print()
'''
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

for num in num_pad:
    for element in num:
        print(element, end=" ")
    print()