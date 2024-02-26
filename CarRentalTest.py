import unittest
from datetime import date
from main.rental.Car import Car
from main.rental.Criteria import Criteria
from main.rental.Renter import Renter
from main.rental.CarRentalCompany import CarRentalCompany

# Create car rental facade
car_rental = CarRentalCompany()

# Create cars and add them to the car rental system
CAR1 = Car("VW", "Golf", "XX11 1UR", "B2", 90)
CAR2 = Car("VW", "Passat", "XX12 2UR", "C1", 110)
CAR3 = Car("VW", "Polo", "XX13 3UR", "A1", 65)
CAR4 = Car("VW", "Polo", "XX14 4UR", "A1", 70)

car_rental.add_car(CAR1)
car_rental.add_car(CAR2)
car_rental.add_car(CAR3) 
car_rental.add_car(CAR4) 

criteria = Criteria()

print("story1:")
matching_cars = car_rental.matching_cars(criteria)
for car in matching_cars:
    print(f"\t{car.make} {car.model}")



