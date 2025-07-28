#====Shopping cart Application====
#core features
#=============
#user should be able to view the available products
#Allow user to items to their cart by providing the product name(validations)
#User should be able to view the current cart items
#remove items from the cart
#checkout --> list all the items upon checkout
#user should be able to clear the entire
#exit
from tokenize import endpats

# Shopping Cart Application
RED = '\033[31m'

products = ["pen","eraser","book","cutter","ruler"]
add_products = []

print("""
====================================================
            C Clarke Shopping App
====================================================
""")
admin = "admin"
password = "password"

user_name = input("Enter the username: ").lower()
user_password = input("Enter the password: ").lower()
if user_name == admin and user_password == password:
    print(RED+"""
====================================================
        Welcome-C-Clarke-Shopping-App
====================================================
    1. Available products
    2. Add products into cart
    3. Check cart
    4. Remove products in cart 
    5. Exit
====================================================  
""")
    user_input = int(input("which option you want to check? : "))
    while True:
        if user_input == 1:
            print(products)
            user_input = int(input("which option you want to check? : "))
        elif user_input == 2:
            while True:
                user_input = input("which products you want to add? : ")
                add_products.append(user_input)
                if user_input == "y":
                    break
            del add_products[-1]
            print(add_products)
            user_input = int(input("You are now add products page, which option you want to check? : "))
        elif user_input == 3:
            print(add_products)
            user_input = int(input("You are now cart page, which option you want to check? : "))
        elif user_input == 4:
            add_products.clear()
            user_input = int(input("You are now remove cart page, which option you want to check? : "))
        else:
            exit()
else:
    print(RED+"Sorry.. your credentials are wrong..")
