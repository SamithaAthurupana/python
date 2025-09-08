from repository import InMemoryProductRepository, InMemoryOrderRepository,InMemoryCustomerRepository
from service import SuperMarketService

service = SuperMarketService(
    product = InMemoryProductRepository(),
    customer = InMemoryCustomerRepository(),
    order = InMemoryOrderRepository()
)
def add_products():
    try:
        prod_id = input("Enter your id: ")
        name = input("Enter your name: ")
        price = float(input("Enter your price: "))
        quantity = int(input("Enter your quantity: "))

        product = service.add_product(prod_id, name, price, quantity)
        print(f"Product {product.name} added successfully!")
    except ValueError as e:
        print("Type Error Occurred "+ str(e))
    except SuperMarketService as e:
        print(e)

def add_customer():
    try:
        cust_id = input("Enter customer id: ")
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        contact = input("Enter customer contact number: ")

        service.add_customer(cust_id, name, email, contact)

    except SuperMarketService as e:
        print(e)

def list_product():
    for prod in service.get_products():
        print(f"Product - ID -{prod.product_id} Product Name - {prod.name}"
              f"Quantity Available{prod.quantity} Product price - {prod.price}")


def create_order():
    try:
        print("Available customers!")
        for cust in service.get_customers




while True:
    print(
        """
        1. ADD PRODUCT
        2. ADD CUSTOMER
        3. LIST PRODUCTS
        4. CREATE ORDER
        5. ADD ITEM TO ORDER
        """)

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_products()
    if choice == 2:
        add_customer()