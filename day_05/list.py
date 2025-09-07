# Python list is a dynamic array (can grow/shrink; not fixed size)
book_name = ["science", "maths", "history", "IT", "commerce", "SFT", "LAW"]

print(book_name)           # print the whole list
print(book_name[0])        # access the first element (indexing starts at 0)

book_name[6] = "ET"        # overwrite the item at index 6 (7th item -> "LAW" becomes "ET")
print(book_name)           # show the updated list

print(len(book_name))      # number of items in the list

print(book_name[-1])       # access the last element (negative index)
print(book_name[-2])       # access the second-to-last element

# Iterate over the list and print each individual item
for name in book_name:
    print(name)

book_name.append("silo")           # add a value at the end of the list
book_name.insert(2, "Atomic")      # insert a value at a specific index (here, index 2)
print(book_name)                   # show list after append + insert

# Delete by index using 'del' (does not return the removed value)
deleted_with_del = book_name[1]    # grab the value so we can show what was deleted
del book_name[1]
print("Deleted with del:", deleted_with_del)

# Delete by index using 'pop' (returns the removed value)
popped_value = book_name.pop(1)
print("Deleted with pop:", popped_value)

print(book_name)                   # final state of the list

#print(help(book_name))


'''numbers_list = []
total = 0

while True:
    get_user_input = int(input("Give the numbers: (enter '0' to exit): "))

    if get_user_input == 0:
        break

    numbers_list.append(get_user_input)

for number in numbers_list:
    total += number
print(total)
'''
'''choice = 2
products = ["apple", "banana", "orange", "grapes", "milk"]
cart = []
item = input("Enter product name to add: ").lower()
while True:
    if item == 0:
        break
    else:
        item = input("Enter product name to add: ").lower()
        if item in products:
            cart.append(item)
            print(f"{item} added to cart.")
        else:
            print("Product not found!")
            item = input("Enter product name to add: ").lower()'''

'''name = ["science", "maths", "history", "IT", "commerce", "SFT"]
for list_in_sen in name:
    print(f"{list_in_sen}", end=" ")'''