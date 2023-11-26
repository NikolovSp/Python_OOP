from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    CONDITIONER_ON = 0.9

    def drive(self, distance: float) -> None:
        fuel_required = (self.fuel_consumption + self.__class__.CONDITIONER_ON) * distance
        if fuel_required <= self.fuel_quantity:
            self.fuel_quantity -= fuel_required

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def drive(self, distance):
        fuel_required = (self.fuel_consumption + 1.6) * distance
        if fuel_required <= self.fuel_quantity:
            self.fuel_quantity -= fuel_required

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
