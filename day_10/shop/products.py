products = [
    {"id": 1, "name": "mini pizza", "price": 200.0},
    {"id": 2, "name": "chicken burger", "price": 400.0},
    {"id": 3, "name": "hamburger", "price": 350.0},
    {"id": 4, "name": "submarine", "price": 175.0},
    {"id": 5, "name": "crunchy chips", "price": 150.0},
    {"id": 6, "name": "fish rolls", "price": 100.0},
    {"id": 7, "name": "bread with curry", "price": 300.0},
    {"id": 8, "name": "lava cake", "price": 650.0},
    {"id": 9, "name": "potato fingers", "price": 250.0}
]

def show_products():
    print("\n📦 Available Products")
    for product in products:
        print(f"{product['id']} - {product['name']} - Rs.{product['price']}")

def find_products_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None
