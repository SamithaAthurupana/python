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

# Shopping Cart Application

# Shopping Cart Application
RED = '\033[31m'

products = ["apple", "banana", "orange", "grapes", "milk"]
cart = []

while True:
    print("=== Shopping Cart Menu ===\n")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove from Cart")
    print("5. Checkout")
    print("6. Clear Cart")
    print("7. Exit")

    choice = input("Choose an option [1-7]: ")

    if choice == "1":
        print("\nAvailable Products:")
        for p in products:
            print(f"- {p}")

    elif choice == "2":
        item = input("Enter product name to add: ").lower()
        if item in products:
            cart.append(item)
            print(f"{item} added to cart.")
        else:
            print("Product not found!")

    elif choice == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in cart:
                print(f"- {item}")

    elif choice == "4":
        item = input("Enter product name to remove: ").lower()
        if item in cart:
            cart.remove(item)
            print(f"{item} removed from cart.")
        else:
            print(RED+"Item not in cart.")

    elif choice == "5":
        if not cart:
            print("Cart is empty.")
        else:
            print("\nCheckout - Items in your cart:")
            for item in cart:
                print(f"- {item}")
            print("Thank you for shopping!")

    elif choice == "6":
        cart.clear()
        print(RED+"Cart cleared.")

    elif choice == "7":
        print(RED+"Exiting...")
        break

    else:
        print(RED+"Invalid choice. Try again.")
