from  nalin_auto import car_inventry, customer_inventry, orders

while True:

    print("""
    ----- Welcome Nalin Auto -----
    
    * Press 1 to view car inventory
    * Press 2 to add a car
    * Press 3 to search a car by name
    * Press 4 to add a add a customer
    * Press 5 to view customer list
    * Press 6 to view customer by ID
    * Press 7 to Add customer order
    """)

    choice = int(input("\n Enter what you wish: "))

    if choice == 1:
        car_inventry.view_cars()

    if choice == 2:
        user_inputs = []
        for field in ["id", "name", "manufacture_year", "model", "price", "country_of_origin"]:
            user_input = input(f"Enter Value for {field}: ")
            user_inputs.append(user_input)

        car_id, name, manuf_year, model, price, country = user_inputs

        car = {
            "id": int(car_id),
            "name": name,
            "manufacture_year": int(manuf_year),
            "model": model,
            "price": float(price),
            "country_of_origin": country
        }

        car_inventry.add_car(car)
        print("Car added successfully..")

    if choice == 3:
        model = input(" Enter the model: ")
        if car_inventry.find_cars_by_model(model) is not None:
            for car in car_inventry.find_cars_by_model(model):
                print(f"Car Name - {car['model']} manufacture in - {car['manufacture_year']} - country - {car['country_of_origin']}")

    if choice == 4:
        user_inputs = []
        for field in ["id", "name", "birth_year"]:
            user_input = input(f"Enter Value for {field}: ")
            user_inputs.append(user_input)

        cust_id, name, birth_year = user_inputs

        customer = {
            "id": int(cust_id),
            "name": name,
            "birth_year": int(birth_year),
            "purchases": []
        }

        customer_inventry.add_customer(customer)
        print("Customer added successfully-----")

    if choice == 5:
            customer_inventry.view_customers()

    if choice == 6:
        cust_id = int(input(" Enter the customer Id: "))
        customer = customer_inventry.get_customer_by_id(cust_id)

        if customer:
            print(f"{customer['id']} - {customer['name']} - {customer['birth_year']}")
            if customer['purchases']:
                for car in customer['purchases']:
                    print(f"  {car['name']} ({car['manufacture_year']}) - {car['model']} - ${car['price']}")
            else:
                print("  No purchases yet")
        else:
            print("Customer not found!")

    if choice == 7:
        cust_id = int(input(" Enter the customer Id: "))
        customer = customer_inventry.get_customer_by_id(cust_id)

        if customer:
            print("\nAvailable cars: ")
            car_inventry.view_cars()

            car_id = int(input("\nEnter the car ID to add to customer: "))
            car = car_inventry.find_cars_by_id(car_id)

            if car:
                customer_inventry.add_customer_order(cust_id,car)
                print(f"Car '{car['name']}'added to {customer['name']}'s purchases")
            else:
                print("Car not found!")
        else:
                print("Customer not found!")




