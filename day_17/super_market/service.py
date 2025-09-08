from dataclasses import dataclass
from typing import List
from model import Product, OrderItem, Order, Customer, SuperMarkerError
from repository import OrderRepository, ProductRepository, CustomerRepository


@dataclass
class SuperMarketService:
    # 🔑 These are repositories (abstract classes/interfaces).
    # This makes the service independent of the actual storage (in-memory, database, etc.).
    product: ProductRepository
    customer: CustomerRepository
    order: OrderRepository

    # Product ------------------
    def add_product(self, product_id: str, name: str, price: float, quantity: int) -> Product:
        # ✅ Validation: check if product already exists
        if self.product.get_product_by_id(product_id) is not None:
            raise SuperMarkerError("Product already exists")

        # ✅ Validation: quantity and price must be non-negative
        if quantity < 0:
            raise SuperMarkerError("Quantity cannot be less than zero")
        if price < 0:
            raise SuperMarkerError("Price cannot be less than zero")

        # ✅ Create and store new product
        product = Product(product_id, name, price, quantity)
        self.product.add(product)
        return product

    def get_all_available_products(self) -> List[Product]:
        # ✅ Filter: only return products that are still in stock
        return [p for p in self.product.list_all() if p.is_available()]

    def get_products(self) -> List[Product]:
        # ✅ Return everything (no filter)
        return self.product.list_all()

    # Customer ------------------
    def add_customer(self, customer_id: str, name: str, email: str, contact: str) -> Customer:
        # ✅ Validation: prevent duplicate customers
        if self.customer.get_customer_by_id(customer_id) is not None:
            raise SuperMarkerError("Customer already exists")

        # ✅ Create and store customer
        customer = Customer(customer_id, name, email, contact)
        self.customer.add(customer)
        return customer

    # Order ------------------
    def add_order(self, order_id: str, customer_id: str) -> Order:
        # ✅ Validation: prevent duplicate orders
        if self.order.get_order_by_id(order_id) is not None:
            raise SuperMarkerError("Order already exists")

        # ✅ Ensure customer exists before creating an order
        cust = self.customer.get_customer_by_id(customer_id)
        if cust is None:
            raise SuperMarkerError("Customer doesn't exist")

        # ✅ Create an order linked to customer (note: use customer's NAME here, not ID)
        order = Order(order_id, customer_id, customer_name=cust.name)
        self.order.add(order)
        return order

    def add_item_to_order(self, order_id: str, product_id: str, quantity: int) -> None:
        # ✅ Fetch order and product
        order = self.order.get_order_by_id(order_id)
        product = self.product.get_product_by_id(product_id)

        # ✅ Validation: check order and product existence
        if order is None:
            raise SuperMarkerError("Order doesn't exist")
        if product is None:
            raise SuperMarkerError("Product doesn't exist")

        # ✅ Validation: check stock
        if product.quantity < quantity:
            raise SuperMarkerError(f"Not enough {product.name} left")

        # ✅ Create order item and add it to order
        order_item = OrderItem(product_id, product.name, quantity, product.price)

        # Flexible: either call `add_item()` if defined OR just append to items list
        if hasattr(order, "add_item"):
            order.add_item(order_item)
        else:
            order.items.append(order_item)

        # ✅ Reduce product stock after purchase
        product.reduce_quantity(quantity)
        self.product.update(product)

        # ✅ Save updated order back to repository
        self.order.update(order)
def get_all_customers(self) -> List[Customer]:
