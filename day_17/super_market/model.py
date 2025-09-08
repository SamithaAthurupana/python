# IMPORTS ----------------
from dataclasses import dataclass, field    # dataclass helper + field for default mutable fields
from typing import List                    # Type hinting for lists


# CUSTOM EXCEPTION ----------------
class SuperMarkerError(Exception):         # Define a custom exception for business-rule violations
    """Raised when a supermarket business rule is violated (e.g., not enough stock)."""
    pass                                   # No extra behaviour; inherits from Exception


# PRODUCT CLASS ----------------
@dataclass
class Product:
    product_id: str        # Unique ID for the product
    name: str              # Human-friendly product name
    price: float           # Price per unit
    quantity: int          # Current stock/available quantity

    def is_available(self) -> bool:
        """Return True if at least one unit is available."""
        return self.quantity > 0

    def add_quantity(self, amount: int) -> None:
        """Increase stock by `amount`. Reject negative amounts."""
        if amount < 0:                          # Validate argument
            raise ValueError("amount to add must be non-negative")
        self.quantity += amount                 # Increase the stored quantity

    def reduce_quantity(self, amount: int) -> None:
        """Decrease stock by `amount`. Raise SuperMarkerError if insufficient stock."""
        if amount < 0:                          # Validate argument
            raise ValueError("amount to reduce must be non-negative")
        if amount > self.quantity:              # If we try to remove more than available
            # Helpful message that shows current available quantity
            raise SuperMarkerError(f"Not enough stock to reduce. Available: {self.quantity}")
        self.quantity -= amount                 # Reduce the stored quantity


# ---------------- CUSTOMER CLASS ----------------
@dataclass
class Customer:
    cust_id: str           # Unique customer ID
    name: str              # Customer full name
    email: str             # Customer email
    phone: str             # Customer phone number (string to preserve leading zeros and formatting)


# ---------------- ORDER ITEM CLASS ----------------
@dataclass
class OrderItem:
    product_id: str        # Product ID being ordered
    product_name: str      # Name of the product at time of ordering (snapshot)
    quantity: int          # Quantity ordered
    unit_price: float      # Price per unit at the time of order

    def total_price(self) -> float:
        """Return total price for this order line (quantity * unit_price)."""
        return self.quantity * self.unit_price


# ---------------- ORDER CLASS ----------------
@dataclass
class Order:
    order_id: str                                 # Unique order ID
    customer_id: str                              # Customer's ID who placed the order
    customer_name: str                            # Customer's name (human readable)
    items: List[OrderItem] = field(default_factory=list)  # List of OrderItem, default empty list

    def add_item(self, item: OrderItem) -> None:
        """Add an OrderItem to the order's items list."""
        # we use a distinct method name (add_item) for clarity (was add_order before)
        self.items.append(item)

    def total_amount(self) -> float:
        """Calculate the total cost of the order by summing each item's total."""
        total = 0.0                               # start accumulator
        for item in self.items:                   # iterate each item
            total += item.total_price()           # add line total
        return total                              # return computed total

    def item_count(self) -> int:
        """Return number of distinct OrderItem lines in the order (not total quantity)."""
        return len(self.items)                    # integer count of item lines

    def item_quantity(self, product_id: str) -> int:
        """Return total quantity for a given product_id in this order (sums multiple lines)."""
        total_qty = 0                             # accumulator for quantity
        for item in self.items:                   # loop through each order line
            if item.product_id == product_id:     # if same product id
                total_qty += item.quantity        # add its quantity
        return total_qty                          # return summed quantity


# ---------------- RUN / DEMO ----------------
if __name__ == '__main__':                      # Only run demo when file executed directly
    # Create a product example
    p = Product(product_id="P001", name="Milk", price=2.5, quantity=10)      # 10 units of Milk
    print("Product created ->", p)                                           # show product state

    # Create a customer example
    c = Customer(cust_id="C001", name="Anura", email="anura@example.com", phone="0771234567")
    print("Customer created ->", c)                                          # show customer state

    # Create an order for that customer
    order = Order(order_id="O001", customer_id=c.cust_id, customer_name=c.name)
    print("Empty order ->", order)                                           # shows empty order

    # Create an order item and add it to order
    oi = OrderItem(product_id=p.product_id, product_name=p.name, quantity=3, unit_price=p.price)
    print("OrderItem created ->", oi)                                        # show order item

    order.add_item(oi)                                                       # add the item to the order
    print("Order after adding item ->", order)                               # order now contains one item

    # Show computed values
    print("Total amount for order:", order.total_amount())                   # 3 * 2.5 = 7.5
    print("Number of item lines in order:", order.item_count())              # 1
    print("Quantity of product P001 in order:", order.item_quantity("P001")) # 3

    # Demonstrate stock change and error handling
    try:
        p.reduce_quantity(5)                 # reduce stock by 5 => remaining 5
        print("Product after reducing 5:", p)
        p.reduce_quantity(10)                # attempt to reduce more than available => raises
    except SuperMarkerError as e:
        print("Caught business error:", e)
