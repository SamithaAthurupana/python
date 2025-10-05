class Vehicles:
    def __init__(self, brand, manufacture_year, fuel_type, ):
        self.brand = brand
        self.manufacture_year = manufacture_year
        self.fuel_type = fuel_type

    def vehicle_sound(self):
        print(f"{self.brand}, is in {self.manufacture_year} using {self.fuel_type}, it sound is smooth")

    def fuel_efficiency(self):
        if self.fuel_type.lower() == "electric":
            print(f"{self.brand} is very efficient (EV).")
        elif self.fuel_type.lower() == "diesel" or "petrol":
            print(f"{self.brand} is moderate in efficiency.")
        else:
            print(f"{self.brand} is average in fuel efficiency.")

class LandVehicles(Vehicles):
    def __init__(self, brand, manufacture_year, fuel_type, no_of_wheels):
        Vehicles.__init__(self, brand, manufacture_year, fuel_type)
        self.no_of_wheels = no_of_wheels

    def get_tyre_pressure(self):
        print(f"{self.brand} has {self.no_of_wheels} then its tyre can handle high Pressure")


class Car(LandVehicles):
    def __init__(self, brand, manufacture_year, fuel_type, no_of_wheels, body_type):
        LandVehicles.__init__(self, brand, manufacture_year, fuel_type, no_of_wheels)
        self.body_type = body_type

    def special_features(self):
        print(f"{self.brand} has good body type of {self.body_type}")

honda = Vehicles("Honda", 1998, "Petrol")
honda.vehicle_sound()
# Honda, is in 1998 using Petrol, its sound is smooth
print(f"{honda.brand:>10}") # right align

dozer = LandVehicles("Satsuma", 1992 , "diesel", 2)
dozer.vehicle_sound()
# Satsuma, is in 1992 using diesel, it sound is smooth

suv = Car("MG ZS", 2018, "petrol", 4, "crossovers")
suv.special_features()
# MG ZS has good body type of crossovers

print(isinstance(honda, Vehicles))
print(isinstance(suv, Vehicles))
print(isinstance(dozer, Vehicles))
# parent class is vehicle then these all comes as True

print(issubclass(Car, LandVehicles))
# W need to add 2 classes to this and we can get True for this because car is sub class of LandVehicles

new_dozer = LandVehicles("Bull machine", 2000, "diesel", 4)
new_dozer.fuel_efficiency()
















