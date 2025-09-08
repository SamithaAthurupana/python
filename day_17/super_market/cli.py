# ---------------- IMPORTS ----------------
from repository import InMemoryProductRepository, InMemoryOrderRepository, InMemoryCustomerRepository
# ✅ මේකෙන් import කරනව in-memory repositories (data ගබඩා කරන්න memory එක යොදා ගන්නවා, DB use කරනව නෑ)

from service import SuperMarketService, SuperMarkerError
# ✅ Service layer (business logic තියන class) සහ error class එක import කරනවා


# ---------------- SERVICE INITIALIZATION ----------------
# ✅ Dependency Injection කියන concept එක මෙතැන use කරනවා
#    Repositories (storage) pass කරනවා service එකට
service = SuperMarketService(
    product=InMemoryProductRepository(),      # Products memory එකේ save වෙනවා
    customer=InMemoryCustomerRepository(),    # Customers memory එකේ save වෙනවා
    order=InMemoryOrderRepository()           # Orders memory එකේ save වෙනවා
)


# ------------------- ADD PRODUCT -------------------
def add_products():
    """User input ගෙන, product එක add කරන function එක"""
    try:
        # ✅ User input ගන්නවා
        prod_id = input("Enter product id: ")           # Product ID
        name = input("Enter product name: ")            # Product name
        price = float(input("Enter product price: "))   # Price -> float convert කරනවා
        quantity = int(input("Enter product quantity: ")) # Quantity -> int convert කරනවා

        # ✅ Service layer එක call කරලා product එක add කරනවා
        product = service.add_product(prod_id, name, price, quantity)

        # Success message
        print(f"Product '{product.name}' added successfully!")

    except ValueError as e:
        # ✅ Wrong data type enter කලොත් (letters instead of numbers)
        print("Type Error: " + str(e))

    except SuperMarkerError as e:
        # ✅ Business logic error (duplicate product, invalid qty/price)
        print("Business Error: " + str(e))


# ------------------- ADD CUSTOMER -------------------
def add_customer():
    """User input ගෙන, customer එක register කරන function එක"""
    try:
        cust_id = input("Enter customer id: ")   # Customer ID
        name = input("Enter customer name: ")    # Name
        email = input("Enter customer email: ")  # Email
        contact = input("Enter customer contact number: ") # Contact number

        # ✅ Service එකට call කරලා customer එක add කරනවා
        customer = service.add_customer(cust_id, name, email, contact)

        print(f"Customer '{customer.name}' added successfully!")

    except SuperMarkerError as e:
        # ✅ Duplicate customers හෝ invalid data errors
        print("Business Error: " + str(e))


# ------------------- LIST PRODUCTS -------------------
def list_product():
    """System එකේ තියන සියලු products print කරනවා"""
    products = service.get_products()   # ✅ Service එකෙන් products list එක ගන්නවා

    if not products:   # ✅ List එක empty නම්
        print("No products available.")
        return

    # ✅ Loop එකෙන් product details print කරනවා
    for prod in products:
        print(f"ID: {prod.product_id} | Name: {prod.name} | "
              f"Quantity: {prod.quantity} | Price: {prod.price}")


# ------------------- CREATE ORDER -------------------
def create_order():
    """Existing customer එකකට order එකක් create කරනවා"""
    try:
        cust_id = input("Enter customer ID for this order: ")   # ✅ Customer ID (exist වෙන එක)
        order_id = input("Enter order ID: ")                    # ✅ Unique Order ID

        # ✅ Service එක call කරලා order එක create කරනවා
        order = service.add_order(order_id, cust_id)

        print(f"Order '{order.order_id}' created for customer '{order.customer_name}'")

    except SuperMarkerError as e:
        # ✅ Error (duplicate order, missing customer)
        print("Business Error: " + str(e))


# ------------------- ADD ITEM TO ORDER -------------------
def add_item_to_order():
    """Existing order එකකට product එකක් add කරනවා"""
    try:
        order_id = input("Enter order ID: ")         # ✅ Order ID
        product_id = input("Enter product ID: ")     # ✅ Product ID
        quantity = int(input("Enter quantity: "))    # ✅ Quantity -> int convert

        # ✅ Service layer එක call කරනවා
        service.add_item_to_order(order_id, product_id, quantity)

        print("Item added to order successfully!")

    except ValueError as e:
        # ✅ Wrong input type (e.g. letters instead of numbers)
        print("Type Error: " + str(e))

    except SuperMarkerError as e:
        # ✅ Not enough stock, order not found, product not found
        print("Business Error: " + str(e))


# ------------------- MAIN MENU LOOP -------------------
# ✅ Program එක run වෙලා continuously user input ගන්නවා
while True:
    print(
        """
        ---------- SUPERMARKET MENU ----------
        1. ADD PRODUCT
        2. ADD CUSTOMER
        3. LIST PRODUCTS
        4. CREATE ORDER
        5. ADD ITEM TO ORDER
        6. EXIT
        """
    )

    try:
        # ✅ User input -> int convert කරනවා
        choice = int(input("Enter your choice: "))

        # ✅ Choice එකට අනුව functions call කරනවා
        if choice == 1:
            add_products()
        elif choice == 2:
            add_customer()
        elif choice == 3:
            list_product()
        elif choice == 4:
            create_order()
        elif choice == 5:
            add_item_to_order()
        elif choice == 6:
            print("Exiting system... Thank you!")
            break   # ✅ Loop එකෙන් break වෙලා program එක exit වෙනවා
        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        # ✅ User input number එකක් නෙමෙයි නම්
        print("Please enter a number between 1 and 6.")
