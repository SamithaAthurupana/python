#nexted loop
'''for y in range(3):
    for x in range(1, 10):
        print(x, end=" ")
    print("|")
print("""1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9
        1 2 3 4 5 6 7 8 9 """)'''


'''rows = int(input("Enter the value for row: "))
column = int(input("Enter the value for column: "))
symbol = input("Enter the value for symbol: ")

for r in range(rows):
    for c in range(column):
        print(symbol, end="")
    print()
    
print("""
        Enter the value for row: 3
        Enter the value for column: 3
        Enter the value for symbol: @
        
        @@@
        @@@
        @@@
        """)'''

# Collection = single "variable" used to store multiple values
#              List = [] ordered and changeable. duplicates OK
#              Set  = {} unordered and immutable, but Add/Remove Ok. No duplicates
#              Tuple= () ordered and unchangeable. Duplicates OK. Faster
'''
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)   #['apple', 'orange', 'banana', 'coconut']
print(fruits[0])
print(fruits[::-1]) #['coconut', 'banana', 'orange', 'apple']

for x in fruits:
    print(x)

print(len(fruits)) #4
print("apple" in fruits) #True

fruits[0] = "pineapple"
for x in fruits:
    print(x, end=" ") #pineapple orange banana coconut
print()

fruits.append("mango")
for x in fruits:
    print(x, end=" ") #pineapple orange banana coconut mango
print()

fruits.sort()
print(fruits) #['banana', 'coconut', 'mango', 'orange', 'pineapple']

fruits.reverse()
print(fruits) #['pineapple', 'orange', 'mango', 'coconut', 'banana']

print(fruits.count("orange")) #1
'''

#shopping cart program
'''
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to buy (q to quite): ").lower()
    if food == "q":
        break
    else:
        price = float(input("Enter the price: $"))
        foods.append(food)
        prices.append(price)
print("------ Your cart ----")

for food in foods:
    print(food, end=" ")
print()

for price in prices:
    total += price
print(f"\ntotal is : ${total}")
'''

#dictionary = a collection of { Key:value } pairs
#             ordered and changeable. No duplicates.

capitals = {"USA": "washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
'''print(capitals.get("USA"))
print(f"capyals : {capitals.keys()}")
for i in capitals.values():
    print(i, end=" ") #washington D.C New Delhi Beijing Moscow

capitals.update({"Germany": "Berlin"})
#capitals.popitem()
print(capitals)

for key, value in capitals.items():
    print(f"{key} : {value}")
'''
'''print("""
        USA : washington D.C
        India : New Delhi
        China : Beijing
        Russia : Moscow
        Germany : Berlin""")'''

# Concession stand program
'''
menu = {"pizza" : 3.00,
        "nachos" : 4.00,
        "soda" : 2.00}

cart = []
total = 0

print("------- Menu --------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("---------------------")

while True:
    food = input("Select item ( q to quite ) : ").lower()

    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("---------------------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")'''

# functions = A block of reusable code
#             place () after the function name to invoke it

'''def happy_birthday(name):
    print(f"happy birth day {name}")

happy_birthday("bro")'''
'''
def display_invoice(user_name, amount, due_date):
    print(f"hello {user_name}")
    print(f"your amount is ${amount:.2f}")
    print(f"your due date is: {due_date}")


display_invoice("samitha", 23.330,"21-09-2025")'''

# return = statement used to end a function
#          and send a result back to the caller
'''
def add1(x , y):
    z = x+y
    return z

def multiply1(x,y):
    z = x*y
    return z

def subtraction(x,y):
    z = x-y
    return z

print(add1(2,4))
print(multiply1(2,4))
print(subtraction(2,4))'''
'''
def create_name(first_name,last_name):
    first_name = first_name.upper()
    last_name = last_name.upper()
    return first_name + " " + last_name

print(create_name("samitha","athurupana"))
'''

# default argument = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces # of arguments
#                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary
'''
def net_price(list_price, discount = 0, tax = 0.5):
    return list_price * (1-discount) * (1 + tax)

print(net_price(300,10.2,0))
print(net_price(300))
print(net_price(300,50.9))'''

'''import time
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(10)'''
'''
def hello(greeting, title, first, last):
    print(f"{greeting}{title} {first}{last}")


hello("hello ",first="samitha ",last="Athurupana",title="Mr.")
'''
'''
# separate argument with print

print("1","2","3","4","5", sep=" * ")'''
'''
def get_phone(country, area, first, last):
    return f"+{country} {area}-{first}-{last}"

phone = get_phone(first=120,area=74,country=+94,last=9663)
print(phone)'''

'''
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,4,6,7,8))'''
'''

#   tuple output - *args
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("samitha", "athurupana")'''
'''

#   dictionary output - **kwargs
def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

address(street="230/A, Meewanapalana", city="horana",state="kalutara", zip ="12424")
'''

'''
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key} : {value}")

shipping_label("Dr.", "samitha", "Athurupana",
               street="230/A, Meewanapalana", city="horana",state="kalutara", zip ="12424")
'''















