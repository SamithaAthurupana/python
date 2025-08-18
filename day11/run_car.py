from  nalin_auto import car_inventry, customer_inventry, orders

while True:

    print("""
    Welcome Nalin Auto 
    
    1.) Press 1 to view inventory
    2.) Press 2 to add a car
    3.) Press 3 to search a car by name
    4.) Press 4 to search a add a customer
    """)

    choice = int(input("\n Enter choice: "))

    if choice == 1:
        car_inventry.view_cars()

    user_inputs = []
    if choice == 2:
        for field in ["id", "name", "manufacture_year", "model", "price", "country_of_origin"]:
            user_input = input(f"Enter Value for {field}")
            user_inputs.append(user_input)

            car_id,name,manuf_year,model,price,country = user_inputs

            car_inventry.add_car({"id": car_id, "name": name, "manufacture_year": manuf_year, "model": model, "price": price, "country_of_origin": country})
    if choice == 3:
        model = input("")
        if car_inventry.find_cars_by_model(model) != None:
            for car in car_inventry.find_cars_by_model(model):
                print(f"Car Name - {car['model']} manufacture in - {car['manufacture_year']} - country - {car['country_of_origin']}")

    if choice == 4:
        for field in ["id", "name", "manufacture_year", "model", "price", "country_of_origin"]:
            user_input = input(f"Enter Value for {field}")
            user_inputs.append(user_input)


