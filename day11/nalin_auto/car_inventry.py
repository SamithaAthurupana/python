cars = [
    {"id" : 1, "name" : "BMW M-8", "manufacture_year" : 2025,"model" : "BMW", "price" : 138000.0, "country_of_origin" : "USA" },
    {"id" : 2, "name" : "BMW X-5 ", "manufacture_year" : 2024,"model" : "BMW", "price" : 55300.0, "country_of_origin" : "GERMANY" },
    {"id" : 3, "name" : "BMW X-4 ", "manufacture_year" : 2023,"model" : "bmw", "price" : 42800.0, "country_of_origin" : "GERMANY" },
    {"id": 4, "name": "BMW X-2 ", "manufacture_year": 2025, "model": "BMW", "price": 42700.0, "country_of_origin": "GERMANY"},
    {"id": 5, "name": "BMW 7 SERIES ", "manufacture_year": 2025, "model": "BMW", "price": 97300.0, "country_of_origin": "GERMANY"},
    {"id": 6, "name": "BMW I-7 ", "manufacture_year": 2023, "model": "bmw", "price": 105700.0, "country_of_origin": "USA"},
    {"id": 4, "name": "BMW 4 SERIES ", "manufacture_year": 2022, "model": "BMW", "price": 78500.0, "country_of_origin": "USA"}
]

def view_cars():
    print("\nAvailable Cars")
    for car in cars:
        print(f"{car['id']} - {car['name']} - {car['manufacture_year']} - {car['model']} - {car['price']} - {car['country_of_origin']} ")

def find_cars_by_id(car_id):
    for car in cars:
        if car["id"] == car_id:
            return car
    return None

def add_car(car):
    cars.append(car)

def find_cars_by_model(car_model):
    searched_items = []
    for car in car_model:
        if car_model == car['model']:
            searched_items.append(car)

    if len(searched_items) > 0:
        return searched_items

    return None

if __name__ == "__main__":
    view_cars()
    products = find_cars_by_id(1)
    #print(cars)