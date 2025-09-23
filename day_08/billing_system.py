# ----- Billing System -----

def get_customer_details():
    """Get input details from customer"""
    name = input("Enter your name: ")
    price = int(input("Enter the price: $"))
    quantity = int(input("Enter the quantity: "))
    membership_input = input("Are you a member? (yes/no): ")
    is_member = membership_input.lower() == "yes"
    return name, price, quantity, is_member


def calculate_total_price(price, quantity):
    """Calculate total price (before discount)"""
    return price * quantity


def calculate_final_price(total , is_member):
    """Apply membership discount if eligible"""
    if total > 5000 and is_member:
        return total * 0.8   # 20% discount
    return total


def print_final_bill(name, price, quantity, total, final_price):
    """Print the full bill with details"""
    print("\n----- Final Bill -----")
    print(f"Customer: {name}")
    print(f"Unit Price: ${price}")
    print(f"Quantity: {quantity}")
    print(f"Total Price: ${total}")
    print(f"Final Price (after discount if any): ${final_price}")


def main():
    """Main function to run billing system"""
    print("----- Welcome to Billing System -----")
    name, price, quantity, is_member = get_customer_details()
    total = calculate_total_price(price= price, quantity = quantity)
    final_price = calculate_final_price(total, is_member)
    print_final_bill(name, price, quantity, total, final_price)


# Run program
main()
