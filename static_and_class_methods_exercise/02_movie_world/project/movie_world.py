from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        cur_customer = [c for c in self.customers if c.id == customer_id][0]
        cur_dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if cur_dvd in cur_customer.rented_dvds:
            return f"{cur_customer.name} has already rented {cur_dvd.name}"

        if cur_dvd.is_rented:
            return "DVD is already rented"

        if cur_customer.age < cur_dvd.age_restriction:
            return f"{cur_customer.name} should be at least {cur_dvd.age_restriction} to rent this movie"

        cur_dvd.is_rented = True
        cur_customer.rented_dvds.append(cur_dvd)
        return f"{cur_customer.name} has successfully rented {cur_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        cur_customer = [c for c in self.customers if c.id == customer_id][0]
        cur_dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if cur_dvd in cur_customer.rented_dvds:
            cur_customer.rented_dvds.remove(cur_dvd)
            cur_dvd.is_rented = False
            return f"{cur_customer.name} has successfully returned {cur_dvd.name}"

        return f"{cur_customer.name} does not have that DVD"

    def __repr__(self):
        result = [c.__repr__() for c in self.customers]
        result += [d.__repr__() for d in self.dvds]
        return "\n".join(result)

