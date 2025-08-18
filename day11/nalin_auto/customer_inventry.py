customers = [
    {"id" : 1 , "name" : "perera" , "birth_year" : 1998, "purchases": []},
]

def view_customers():
    print("\nAvailable Customers")
    for customer in customers:
        print(f"{customers['id']} - {customers['name']} - {customers['birth_year']} - {customers['id']}")
