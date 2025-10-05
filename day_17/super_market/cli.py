
from repository import InMemoryProductRepository, InMemoryOrderRepository, InMemoryCustomerRepository
from service import SuperMarketService, SuperMarkerError

# ✅ Dependency Injection කියන concept එක මෙතැන use කරනවා
#    Repositories (storage) pass කරනවා service එකට
service = SuperMarketService(
    product=InMemoryProductRepository(),      # Products memory එකේ save වෙනවා
    customer=InMemoryCustomerRepository(),    # Customers memory එකේ save වෙනවා
    order=InMemoryOrderRepository()           # Orders memory එකේ save වෙනවා
)


def add_products():
    try:
        prod_id = input("Enter product id: ")           # Product ID
        name = input("Enter product name: ")            # Product name
        price = float(input("Enter product price: "))   # Price -> float convert කරනවා
        quantity = int(input("Enter product quantity: ")) # Quantity -> int convert කරනවා

        product = service.add_product(prod_id, name, price, quantity) # ✅ Service layer එක call කරලා product එක add කරනවා
        print(f"Product '{product.name}' added successfully!") # Success message

    except ValueError as e:
        print("Type Error: " + str(e)) # ✅ Wrong data type enter කලොත් (letters instead of numbers)

    except SuperMarkerError as e:
        print("Business Error: " + str(e)) # ✅ Business logic error (duplicate product, invalid qty/price)


def add_customer():
    try:
        cust_id = input("Enter customer id: ")   # Customer ID
        name = input("Enter customer name: ")    # Name
        email = input("Enter customer email: ")  # Email
        contact = input("Enter customer contact number: ") # Contact number

        customer = service.add_customer(cust_id, name, email, contact) # ✅ Service එකට call කරලා customer එක add කරනවා
        print(f"Customer '{customer.name}' added successfully!")

    except SuperMarkerError as e:
        print("Business Error: " + str(e)) # ✅ Duplicate customers හෝ invalid data errors


def list_product():
    products = service.get_products()   # ✅ Service එකෙන් products list එක ගන්නවා

    if not products:   # ✅ List එක empty නම්
        print("No products available.")
        return

    for prod in products: # ✅ Loop එකෙන් product details print කරනවා
        print(f"ID: {prod.product_id} | Name: {prod.name} | "
              f"Quantity: {prod.quantity} | Price: {prod.price}")


def create_order():
    try:
        cust_id = input("Enter customer ID for this order: ")   # ✅ Customer ID (exist වෙන එක)
        order_id = input("Enter order ID: ")                    # ✅ Unique Order ID

        order = service.add_order(order_id, cust_id) # ✅ Service එක call කරලා order එක create කරනවා
        print(f"Order '{order.order_id}' created for customer '{order.customer_name}'")

    except SuperMarkerError as e:
        print("Business Error: " + str(e))   # ✅ Error (duplicate order, missing customer)


def add_item_to_order():
    try:
        order_id = input("Enter order ID: ")         # ✅ Order ID
        product_id = input("Enter product ID: ")     # ✅ Product ID
        quantity = int(input("Enter quantity: "))    # ✅ Quantity -> int convert

        service.add_item_to_order(order_id, product_id, quantity) # ✅ Service layer එක call කරනවා
        print("Item added to order successfully!")

    except ValueError as e:
        print("Type Error: " + str(e)) # ✅ Wrong input type (e.g. letters instead of numbers)

    except SuperMarkerError as e:
        print("Business Error: " + str(e))  # ✅ Not enough stock, order not found, product not found


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
        choice = int(input("Enter your choice: "))

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
            break
        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Please enter a number between 1 and 6.") # ✅ User input number එකක් නෙමෙයි නම්
