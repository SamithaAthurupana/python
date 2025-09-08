from abc import ABC, abstractmethod
from typing import List, Dict
from model import Product, Customer, Order


# PRODUCT REPOSITORY --------------------
class ProductRepository(ABC):   # Abstract base class for product storage

    @abstractmethod
    def add(self, product: Product):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: str) -> Product:
        pass

    @abstractmethod
    def list_all(self) -> List[Product]:
        pass

    @abstractmethod
    def update(self, product: Product):
        pass


# CUSTOMER REPOSITORY --------------------
class CustomerRepository(ABC):

    @abstractmethod
    def add(self, customer: Customer):
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id: str) -> Customer:
        pass

    @abstractmethod
    def list_all(self) -> List[Customer]:
        pass


# ORDER REPOSITORY --------------------
class OrderRepository(ABC):

    @abstractmethod
    def add(self, order: Order):
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def list_all(self) -> List[Order]:
        pass

    @abstractmethod
    def update(self, order: Order):
        pass


# -------------------- IN-MEMORY IMPLEMENTATIONS --------------------

class InMemoryProductRepository(ProductRepository):

    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add(self, product: Product):
        self.products[product.product_id] = product

    def get_product_by_id(self, product_id: str) -> Product:
        return self.products.get(product_id)

    def list_all(self) -> List[Product]:
        return list(self.products.values())

    def update(self, product: Product):
        self.products[product.product_id] = product


class InMemoryCustomerRepository(CustomerRepository):

    def __init__(self):
        self.customers: Dict[str, Customer] = {}

    def add(self, customer: Customer):
        self.customers[customer.cust_id] = customer

    def get_customer_by_id(self, customer_id: str) -> Customer:
        return self.customers.get(customer_id)

    def list_all(self) -> List[Customer]:
        return list(self.customers.values())


class InMemoryOrderRepository(OrderRepository):

    def __init__(self):
        self.orders: Dict[str, Order] = {}

    def add(self, order: Order):
        self.orders[order.order_id] = order

    def get_order_by_id(self, order_id: str) -> Order:
        return self.orders.get(order_id)

    def list_all(self) -> List[Order]:
        return list(self.orders.values())

    def update(self, order: Order):
        self.orders[order.order_id] = order
