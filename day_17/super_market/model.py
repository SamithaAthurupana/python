import datetime
from dataclasses import dataclass, field
from typing import List, Optional

class SuperMarkerError(Exception):
    pass

# ---------------- PRODUCT CLASS ----------------
@dataclass
class Product:
    product_id: str   # Unique ID for the product
    name: str         # Name of the product
    price: float      # Price per unit
    quantity: int     # Current stock/available quantity

    def is_available(self) -> bool:
        # Returns True if there is at least 1 unit in stock
        return self.quantity > 0

    def add_quantity(self, amount: int):
        # Increase stock by a given amount
        self.quantity += amount

    def reduce_quantity(self, amount: int) -> None:
        # Reduce stock by a given amount
        # If requested amount is more than stock, raise an error
        if amount > self.quantity:
            raise SuperMarkerError(f"Not enough stock to reduce.-{self.quantity}")
        self.quantity -= amount


# ---------------- CUSTOMER CLASS ----------------
@dataclass
class Customer:
    cust_id: str   # Unique customer ID
    name: str      # Customer full name
    email: str     # Customer email
    phone: str     # Customer phone number


# ---------------- ORDER ITEM CLASS ----------------
@dataclass
class OrderItem:
    product_id: str    # Product ID being ordered
    product_name: str  # Name of the product
    quantity: int      # Quantity ordered
    unit_price: float  # Price per unit at the time of order

    def total_price(self) -> float:
        # Calculate total cost of this order item
        return self.quantity * self.unit_price


# ---------------- ORDER CLASS ----------------
@dataclass
class Order:
    order_id: str       # Unique order ID
    customer_id: str    # ID of the customer who placed the order
    customer_name: str  # Name of the customer
    items: List[OrderItem] = field(default_factory=list)  # List of order items

    def add_order(self, order: OrderItem) -> None:
        self.items.append(order)

    def total_amount(self) -> float:
        return sum(item.total_price() for item in self.items)

    def item_count(self) -> float:
        return len(self.items)

    '''def total_amount(self) -> float:
        # Calculate total bill for the order by summing item totals
        
        total = 0.0
        for item in self.items:
            total += item.total_price()
        return total'''

'''    def item_count(self, product_id: str) -> int:
        # Find how many of a specific product (by ID) were ordered
        for item in self.items:
            if item.product_id == product_id:
                return item.quantity
        return 0  # Return 0 if product is not in the order'''


if __name__ == '__main__':
    order = Order("001", "111", "anura")
    print(order)

    order_item = OrderItem("001","111",233,133)
    print(order_item)