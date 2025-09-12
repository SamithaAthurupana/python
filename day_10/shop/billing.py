SERVICE_CHARGE = 0.1
VAT_RATE = 0.18

def calculate_bill(cart_items):
    subtotal = 0
    for item in cart_items.values():   # FIX: use .values() because cart_items is a dict
        subtotal += item["product"]["price"] * item["quantity"]

    service_charge = subtotal * SERVICE_CHARGE
    vat = subtotal * VAT_RATE
    return subtotal, service_charge, vat

def shop_checkout(cart_items):
    if not cart_items:
        print("🛒 Your cart is empty!")
        return

    subtotal, service_charge, vat = calculate_bill(cart_items)

    print("\n##### FINAL BILL #####")
    print(f"Subtotal      : {subtotal}")
    print(f"Service charge: {service_charge}")
    print(f"VAT           : {vat}")
    print(f"Final Amount  : {subtotal + service_charge + vat}")
