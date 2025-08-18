customers = [
    {"id" : 1 , "name" : "perera" , "birth_year" : 1998, "purchases": [{"id": "4", "name": "BMW 4 SERIES ",
    "manufacture_year": 2022, "model": "BMW", "price": 78500.0, "country_of_origin": "USA"}]
    }
]

def add_customee (customer):
    customers.append(customer)

def get_customer_by_id(cust_id):
    for cust in customers:
        if cust['id']  == cust_id:
            return cust
    return None

def add_customer_order(cust_id, car_info):
    if get_customer_by_id(cust_id) != None:

        for cust in customers:
            if cust['id'] == cust_id:
                cust['purchases'].append(car_info)

def view_customers():
    print("\nAvailable Customers")
    for customer in customers:
        print(f"{customers['id']} - {customers['name']} - {customers['birth_year']} - {customers['id']}")
