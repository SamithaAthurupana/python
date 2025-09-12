from shop import billing, cart, products

while True:
    print(
        """
        Welcome to Super city
        1.) Press 1 to view products
        2.) Press 2 to add a product to cart
        3.) Press 3 to view cart
        4.) Press 4 to checkout
        5.) Press 5 to Exit
        """
    )
    choice = int(input("\n Enter choice: "))

    if choice == 1:
        products.show_products()

    elif choice == 2:
        products.show_products()
        products_id = int(input("\n Enter the product Id: "))

        product = products.find_products_by_id(products_id)
        if product is None:
            print("❌ Sorry this product doesn't exist")
        else:
            quantity = int(input("Enter quantity: "))
            cart.add_to_cart(product, quantity)

    elif choice == 3:
        cart.view_cart()

    elif choice == 4:
        billing.shop_checkout(cart.cart_array)

    elif choice == 5:
        print("Thank you for shopping at Super city! 👋")
        break

    else:
        print("⚠️ Invalid choice, please try again!")
