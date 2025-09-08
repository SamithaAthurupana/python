cart_array = {}

def add_to_cart(product, quantity):
    cart_array[product] = quantity
    print(f"{product} X {quantity} added to cart successfully!")

def remove_from_cart(product_id, choice):
    global cart_array
    if choice in range(1,3):
        if choice == 1:
            cart_array = [item for item in cart_array if item["product"]["ID"] != product_id]
            print(f"Removed product id - {product_id}")

        else:
            del cart_array

    else:
        print("Enter a valid number!")

def view_cart():
    for arr in cart_array:
        print(f"""

Your products:
    {arr["name"]}  X  {arr["quantity"]} """)