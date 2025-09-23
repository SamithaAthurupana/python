

SERVICE_CHARGE = 0.1
VAT_RATE = 0.18

def calculate_bill(cart_items):
    subtotal = 0
    for item in cart_items:
        subtotal += item["product"]["price"] * item["quantity"]
    service_charge = subtotal * SERVICE_CHARGE
    # subtotal = sum([item["product"]["price"] * item["quantity"] for item in cart_items])

    vat = subtotal * VAT_RATE

    return subtotal, service_charge, vat

def shop_checkout(cart_items):
    subtotal, service_charge, vat = calculate_bill(cart_items)

    print("##### final bill #####")
    print(f"subtotal - {subtotal}")
    print(f"service charge - {service_charge}")
    print(f"vat - {vat}")
    print(f"final amount - {subtotal + service_charge + vat}")