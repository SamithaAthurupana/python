from dataclasses import dataclass, field    # automatic constructor (__init__) create
from typing import List                    # List type hint (e.g., List[OrderItem])

# CUSTOM EXCEPTION ----------------
class SuperMarkerError(Exception):
    pass    # normal Exception inherit

# PRODUCT CLASS ----------------
@dataclass
class Product:
    product_id: str        # Product unique ID
    name: str              # Product name
    price: float           # Unit price
    quantity: int          # Available stock

    def is_available(self) -> bool: # True/False return
        return self.quantity > 0   # quantity > 0 then return True otherwise False

    def add_quantity(self, amount: int) -> None:
        if amount < 0:   # When negative numbers add attempt will error
            raise ValueError("amount to add must be non-negative")
        self.quantity += amount   # stock add

    def reduce_quantity(self, amount: int) -> None: # reduce item in stock
        if amount < 0:   # Do not accept Negative number reduce
            raise ValueError("amount to reduce must be non-negative")
        if amount > self.quantity:  # can not reduce more than stock
            raise SuperMarkerError(f"Not enough stock to reduce. Available: {self.quantity}")
        self.quantity -= amount   # reduce from stock


@dataclass
class Customer:
    cust_id: str           # Customer ID (unique)
    name: str              # Full name
    email: str             # Email address
    phone: str             # Phone number (string → leading 0 save වෙන්න)

@dataclass
class OrderItem:
    product_id: str        # Product ID (refer to Product)
    product_name: str      # Product name (snapshot of purchase time)
    quantity: int          # How many units ordered
    unit_price: float      # Price per unit at time of order

    def total_price(self) -> float:
        """Single line total = quantity * unit_price"""
        return self.quantity * self.unit_price

@dataclass
class Order:
    order_id: str                                 # Unique order ID
    customer_id: str                              # Which customer placed this order
    customer_name: str                            # Customer’s name
    items: List[OrderItem] = field(default_factory=list)  # Empty list default value

    def add_item(self, item: OrderItem) -> None: # product add to order
        self.items.append(item)   # append → new item to list

    def total_amount(self) -> float:# total cost in order
        total = 0.0                               # accumulator variable එක
        for item in self.items:                   # Loop to all the OrderItem
            total += item.total_price()           # total_price() call and add the item price
        return total                              # return final sum

    def item_count(self) -> int:# different OrderItems count in order (distinct lines)
        return len(self.items)   # items count in list

    def item_quantity(self, product_id: str) -> int:
        total_qty = 0
        for item in self.items:                   # Loop and check every item
            if item.product_id == product_id:     # දාපු product_id එක match වුණොත්
                total_qty += item.quantity        # quantity එක add කරනවා
        return total_qty                          # final total quantity return කරනවා


# ---------------- RUN / DEMO ----------------
if __name__ == '__main__':
    # Product එකක් create කරනවා
    p = Product(product_id="P001", name="Milk", price=2.5, quantity=10)
    print("Product created ->", p)

    # Customer එකක් create කරනවා
    c = Customer(cust_id="C001", name="Anura", email="anura@example.com", phone="0771234567")
    print("Customer created ->", c)

    # Order එකක් create කරනවා (empty order initially)
    order = Order(order_id="O001", customer_id=c.cust_id, customer_name=c.name)
    print("Empty order ->", order)

    # Order item එකක් create කරනවා
    oi = OrderItem(product_id=p.product_id, product_name=p.name, quantity=3, unit_price=p.price)
    print("OrderItem created ->", oi)

    # Order එකට item එක add කරනවා
    order.add_item(oi)
    print("Order after adding item ->", order)

    # Calculations demo
    print("Total amount for order:", order.total_amount())        # ✅ Loop එකෙන් total ගන්නවා
    print("Number of item lines in order:", order.item_count())   # ✅ len() use
    print("Quantity of product P001 in order:", order.item_quantity("P001")) # ✅ Loop එකෙන් qty count

    # Error handling demo
    try:
        p.reduce_quantity(5)   # ✅ stock reduce by 5 → ok
        print("Product after reducing 5:", p)
        p.reduce_quantity(10)  # ✅ stock 10 reduce attempt (අඩුවන stock නෑ → Error throw වෙනවා)
    except SuperMarkerError as e:
        print("Caught business error:", e)
