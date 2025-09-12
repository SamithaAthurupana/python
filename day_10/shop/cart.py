cart_array = {}  # dictionary { product_id : {"product": product, "quantity": qty} }

def add_to_cart(product, quantity):
    product_id = product["id"]
    if product_id in cart_array:
        cart_array[product_id]["quantity"] += quantity
    else:
        cart_array[product_id] = {"product": product, "quantity": quantity}
    print(f"✅ {product['name']} X {quantity} added to cart successfully!")

def remove_from_cart(product_id):
    if product_id in cart_array:
        del cart_array[product_id]
        print(f"🗑️ Removed product id - {product_id}")
    else:
        print("❌ Product not found in cart!")

def view_cart():
    if not cart_array:
        print("🛒 Your cart is empty!")
    else:
        print("\nYour Cart:")
        for item in cart_array.values():
            print(f"- {item['product']['name']}  X  {item['quantity']}")
