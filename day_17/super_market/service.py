from dataclasses import dataclass
from typing import List
from model import Product, OrderItem, Order, Customer, SuperMarkerError

from repository import OrderRepository, ProductRepository, CustomerRepository
# repositories (storage layer interfaces) import


# SERVICE CLASS ----------------
@dataclass
class SuperMarketService:
    # 🔑 Repository objects store කරනවා
    # (Dependency Injection → DB connect වෙනවට instead memory repos දෙන්න පුළුවන්)
    product: ProductRepository
    customer: CustomerRepository
    order: OrderRepository

    # Product ------------------
    def add_product(self, product_id: str, name: str, price: float, quantity: int) -> Product:

        if self.product.get_product_by_id(product_id) is not None: # check product_id, is duplicate?
            raise SuperMarkerError("Product already exists")
        if quantity < 0:      # ✅ validation: stock quantity negative නොවිය යුතුයි
            raise SuperMarkerError("Quantity cannot be less than zero")
        if price < 0:         # ✅ validation: price negative නොවිය යුතුයි
            raise SuperMarkerError("Price cannot be less than zero")


        product = Product(product_id, name, price, quantity) # ✅ create Product object
        self.product.add(product) # ✅ save repository
        return product

    def get_all_available_products(self) -> List[Product]:
        return [p for p in self.product.list_all() if p.is_available()]  # ✅ p.is_available() == True

    def get_products(self) -> List[Product]:
        return self.product.list_all()

    # Customer ------------------
    def add_customer(self, customer_id: str, name: str, email: str, contact: str) -> Customer:
        if self.customer.get_customer_by_id(customer_id) is not None: # ✅ duplicate customer check
            raise SuperMarkerError("Customer already exists")

        customer = Customer(customer_id, name, email, contact) # ✅ Customer object එක create කරනවා
        # ✅ save කරනවා
        self.customer.add(customer)
        return customer

    def get_all_customers(self) -> List[Customer]:
        """ඉන්න customers හැම එකම return කරනවා"""
        return self.customer.list_all()

    # ------------------ Order ------------------
    def add_order(self, order_id: str, customer_id: str) -> Order:
        """නව order එකක් customer එකකට create කරන method එක"""

        # ✅ duplicate order check කරනවා
        if self.order.get_order_by_id(order_id) is not None:
            raise SuperMarkerError("Order already exists")

        # ✅ customer එක exist ද බලනවා
        cust = self.customer.get_customer_by_id(customer_id)
        if cust is None:
            raise SuperMarkerError("Customer doesn't exist")

        # ✅ නව order එක create කරනවා (customer name attach කරලා)
        order = Order(order_id, customer_id, customer_name=cust.name)
        # ✅ save කරනවා
        self.order.add(order)
        return order

    def add_item_to_order(self, order_id: str, product_id: str, quantity: int) -> None:
        """එක order එකකට product එකක් add කරන method එක"""

        # ✅ order එක retrieve කරනවා
        order = self.order.get_order_by_id(order_id)
        # ✅ product එක retrieve කරනවා
        product = self.product.get_product_by_id(product_id)

        # Validation checks
        if order is None:
            raise SuperMarkerError("Order doesn't exist")
        if product is None:
            raise SuperMarkerError("Product doesn't exist")

        # ✅ stock check
        if product.quantity < quantity:
            raise SuperMarkerError(f"Not enough {product.name} left")

        # ✅ OrderItem එක create කරනවා
        order_item = OrderItem(product_id, product.name, quantity, product.price)

        # ✅ order class එකේ add_item() තියෙනවද බලනවා
        if hasattr(order, "add_item"):
            order.add_item(order_item)   # custom method call
        else:
            order.items.append(order_item)   # direct append

        # ✅ product stock එක reduce කරනවා
        product.reduce_quantity(quantity)
        # ✅ updated product save කරනවා
        self.product.update(product)

        # ✅ updated order save කරනවා
        self.order.update(order)
