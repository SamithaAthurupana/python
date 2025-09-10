from abc import ABC, abstractmethod        # ✅ Abstract Base Class (ABC) system එක import කරනවා.
from typing import List, Dict              # ✅ Type hints: List, Dict types import කරනවා.
from model import Product, Customer, Order # ✅ අපේ domain models (Product, Customer, Order) import කරනවා.


# ---------------- PRODUCT REPOSITORY (INTERFACE) ----------------
class ProductRepository(ABC):   # 🟢 Product data store එකක් represent කරන Abstract Base Class
                                # 👉 මෙය කියන්නේ "contract" එකක්. Implement කරන class එකට මේ methods define කරන්නම වෙනවා.

    @abstractmethod
    def add(self, product: Product):
        pass                    # 🟢 Product එකක් add කරන්න abstract method එක

    @abstractmethod
    def get_product_by_id(self, product_id: str) -> Product:
        pass                    # 🟢 Product එක ID එකෙන් retrieve කරන්න abstract method එක

    @abstractmethod
    def list_all(self) -> List[Product]:
        pass                    # 🟢 සියලුම products retrieve කරන්න abstract method එක

    @abstractmethod
    def update(self, product: Product):
        pass                    # 🟢 තිබෙන product එක update කරන්න abstract method එක


# ---------------- CUSTOMER REPOSITORY (INTERFACE) ----------------
class CustomerRepository(ABC):             # 🟢 Customer data store එක represent කරන interface එක

    @abstractmethod
    def add(self, customer: Customer):
        pass                                # 🟢 Customer එකක් add කරන්න abstract method එක

    @abstractmethod
    def get_customer_by_id(self, customer_id: str) -> Customer:
        pass                                # 🟢 Customer එක ID එකෙන් retrieve කරන්න abstract method එක

    @abstractmethod
    def list_all(self) -> List[Customer]:
        pass                                # 🟢 සියලුම customers retrieve කරන්න abstract method එක


# ---------------- ORDER REPOSITORY (INTERFACE) ----------------
class OrderRepository(ABC):                # 🟢 Order data store එක represent කරන interface එක

    @abstractmethod
    def add(self, order: Order):
        pass                                # 🟢 Order එක add කරන්න abstract method එක

    @abstractmethod
    def get_order_by_id(self, order_id: str) -> Order:
        pass                                # 🟢 Order එක ID එකෙන් retrieve කරන්න abstract method එක

    @abstractmethod
    def list_all(self) -> List[Order]:
        pass                                # 🟢 සියලුම orders retrieve කරන්න abstract method එක

    @abstractmethod
    def update(self, order: Order):
        pass                                # 🟢 තිබෙන order එක update කරන්න abstract method එක


# -------------------- IN-MEMORY IMPLEMENTATIONS --------------------
# 👉 මේ classes DB එකක් use නොකර, memory තුළ dictionary එකක data save කරනවා.


class InMemoryProductRepository(ProductRepository):   # 🟢 ProductRepository implement කරනවා
    def __init__(self):
        self.products: Dict[str, Product] = {}        # 🟢 dict එකක් store කරනවා → {product_id: Product}

    def add(self, product: Product):
        self.products[product.product_id] = product   # 🟢 product_id as key, Product object save කරනවා

    def get_product_by_id(self, product_id: str) -> Product:
        return self.products.get(product_id)          # 🟢 dict.get() → product_id තිබුනොත් Product return, නැත්තම් None

    def list_all(self) -> List[Product]:
        return list(self.products.values())           # 🟢 dict.values() → Product objects, list() කරලා return කරනවා

    def update(self, product: Product):
        self.products[product.product_id] = product   # 🟢 dict එකේ තියෙන එක update කරනවා (key එක එකම → overwrite වෙනවා)


class InMemoryCustomerRepository(CustomerRepository):   # 🟢 CustomerRepository implement කරනවා
    def __init__(self):
        self.customers: Dict[str, Customer] = {}        # 🟢 dict එකක් store කරනවා → {cust_id: Customer}

    def add(self, customer: Customer):
        self.customers[customer.cust_id] = customer     # 🟢 cust_id as key, Customer object save කරනවා

    def get_customer_by_id(self, customer_id: str) -> Customer:
        return self.customers.get(customer_id)          # 🟢 dict.get() → customer retrieve කරනවා

    def list_all(self) -> List[Customer]:
        return list(self.customers.values())            # 🟢 සියලුම customers list එකක් return කරනවා


class InMemoryOrderRepository(OrderRepository):         # 🟢 OrderRepository implement කරනවා
    def __init__(self):
        self.orders: Dict[str, Order] = {}              # 🟢 dict එකක් store කරනවා → {order_id: Order}

    def add(self, order: Order):
        self.orders[order.order_id] = order             # 🟢 order_id as key, Order object save කරනවා

    def get_order_by_id(self, order_id: str) -> Order:
        return self.orders.get(order_id)                # 🟢 dict.get() → order retrieve කරනවා

    def list_all(self) -> List[Order]:
        return list(self.orders.values())               # 🟢 සියලුම orders list එකක් return කරනවා

    def update(self, order: Order):
        self.orders[order.order_id] = order             # 🟢 order එක update කරනවා (overwrite)
