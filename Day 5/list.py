#python list is dynamic array, not a fixed size
book_name = ["science", "maths", "history", "IT", "commerce", "SFT", 18]
'''print(book_name)
print(book_name[0])
book_name[6] = "ET"
print(book_name)
print(len(book_name))
print(book_name[-1]) #access the last element
print(book_name[-2]) #access the last element

for i in book_name:
    print(book_name)

book_name.append("silo")  #add value last

book_name.insert(2,"Atomic") #add value into specific index
print(book_name)
del book_name[1]  #delete
book_name.pop(1)
print(book_name)
#print(help(book_name))
'''

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
choice = 2
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
            item = input("Enter product name to add: ").lower()