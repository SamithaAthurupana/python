from dataclasses import dataclass   # ✅ Used to create simple classes with automatic __init__, __repr__, etc.
from typing import List             # ✅ Type hint for lists (e.g., List[Product])
from model import Product, OrderItem, Order, Customer, SuperMarkerError
# ✅ Importing domain models (Product, Order, Customer, etc.) and custom exception (SuperMarkerError)
from repository import OrderRepository, ProductRepository, CustomerRepository
# ✅ Importing repository interfaces (abstract classes). These define how data is stored/fetched.


@dataclass
class SuperMarketService:
    """
    ✅ This is the Service Layer of our app.
    - It contains the *business logic* (rules and validation).
    - It depends on repository interfaces, not real storage.
    - This makes the code flexible: you can switch between
      in-memory, database, or API repositories without changing this class.
    """

    # Repositories (interfaces) injected into the service.
    product: ProductRepository     # For product data operations
    customer: CustomerRepository   # For customer data operations
    order: OrderRepository         # For order data operations

    # ------------------ Product ------------------
    def add_product(self, product_id: str, name: str, price: float, quantity: int) -> Product:
        """Add a new product after validation"""

        # ✅ Check if product already exists (by ID).
        if self.product.get_product_by_id(product_id) is not None:
            raise SuperMarkerError("Product already exists")

        # ✅ Validate quantity must be >= 0
        if quantity < 0:
            raise SuperMarkerError("Quantity cannot be less than zero")

        # ✅ Validate price must be >= 0
        if price < 0:
            raise SuperMarkerError("Price cannot be less than zero")

        # ✅ Create a new Product object with given details
        product = Product(product_id, name, price, quantity)

        # ✅ Add the product into the repository (storage)
        self.product.add(product)

        # ✅ Return the newly created product
        return product

    def get_all_available_products(self) -> List[Product]:
        """Return only products that are in stock"""

        # ✅ Fetch all products, filter only those that are available
        return [p for p in self.product.list_all() if p.is_available()]

    def get_products(self) -> List[Product]:
        """Return all products (no filter)"""

        # ✅ Simply return everything from repository
        return self.product.list_all()

    # ------------------ Customer ------------------
    def add_customer(self, customer_id: str, name: str, email: str, contact: str) -> Customer:
        """Add a new customer after validation"""

        # ✅ Check if customer already exists
        if self.customer.get_customer_by_id(customer_id) is not None:
            raise SuperMarkerError("Customer already exists")

        # ✅ Create a new Customer object
        customer = Customer(customer_id, name, email, contact)

        # ✅ Add customer to repository
        self.customer.add(customer)

        # ✅ Return the new customer
        return customer

    def get_all_customers(self) -> List[Customer]:
        """Return all customers"""

        # ✅ Just return all customers from repository
        return self.customer.list_all()

    # ------------------ Order ------------------
    def add_order(self, order_id: str, customer_id: str) -> Order:
        """Create a new order for a customer"""

        # ✅ Check if order already exists
        if self.order.get_order_by_id(order_id) is not None:
            raise SuperMarkerError("Order already exists")

        # ✅ Ensure that the customer exists
        cust = self.customer.get_customer_by_id(customer_id)
        if cust is None:
            raise SuperMarkerError("Customer doesn't exist")

        # ✅ Create a new Order object linked to the customer
        # Note: use customer.name (not ID) for readability
        order = Order(order_id, customer_id, customer_name=cust.name)

        # ✅ Add the order to repository
        self.order.add(order)

        # ✅ Return the new order
        return order

    def add_item_to_order(self, order_id: str, product_id: str, quantity: int) -> None:
        """Add a product as an item into an existing order"""

        # ✅ Fetch the order by ID
        order = self.order.get_order_by_id(order_id)

        # ✅ Fetch the product by ID
        product = self.product.get_product_by_id(product_id)

        # ✅ If order does not exist, raise error
        if order is None:
            raise SuperMarkerError("Order doesn't exist")

        # ✅ If product does not exist, raise error
        if product is None:
            raise SuperMarkerError("Product doesn't exist")

        # ✅ Check if enough stock is available
        if product.quantity < quantity:
            raise SuperMarkerError(f"Not enough {product.name} left")

        # ✅ Create a new OrderItem (line in the order)
        order_item = OrderItem(product_id, product.name, quantity, product.price)

        # ✅ Add the item into the order
        # If order has its own add_item() method → use it
        if hasattr(order, "add_item"):
            order.add_item(order_item)
        else:
            # Otherwise, directly append to items list
            order.items.append(order_item)

        # ✅ Reduce stock of the product
        product.reduce_quantity(quantity)

        # ✅ Update product in repository (so stock is saved)
        self.product.update(product)

        # ✅ Update order in repository (so order is saved)
        self.order.update(order)
