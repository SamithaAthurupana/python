from shop import billing, cart, products

while True:
    print(
        """
        Welcome toSuper city
        1.) Press 1 to view products
        2.) Press 2 to add a product to cart
        """
    )
    choice = int(input("\n Enter choice: "))

    if choice == 1:
        products.show_products()

    if choice == 2:
        products.show_products()
        products_id = int(input("\n Enter the product Id: "))

        if products.find_products_by_id(products_id) is None:
            print("Sorry this product doesn't exits")
        else:
            quantity = int(input("Enter quantity: "))
            cart.add_to_cart(products.find_products_by_id(products_id),quantity)
    if choice == 3:
        cart.view_cart()

    if choice == 4:
        billing.shop_checkout(cart.cart_items)