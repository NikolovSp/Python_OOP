from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"

        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"
        #
        # try:
        #     found_worker = next(filter(lambda x: x.name == worker_name, self.workers))
        # except StopIteration:
        #     return f"There is no {worker_name} in the zoo"
        #
        # self.workers.remove(found_worker)
        # return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salary = sum([worker.salary for worker in self.workers])
        # total_salary = 0
        # for worker in self.workers:
        #     total_salary += worker.salary

        if total_salary <= self.__budget:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_cost = sum([animal.money_for_care for animal in self.animals])
        # for animal in self.animals:
        #     total_cost += animal.money_for_care

        if total_cost <= self.__budget:
            self.__budget -= total_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(repr(animal))
            else:
                cheetahs.append(repr(animal))

        result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        result.extend(lions)
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return '\n'.join(result)

    def workers_status(self) -> str:
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(repr(worker))
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(repr(worker))
            else:
                vets.append(repr(worker))

        result = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
        result.extend(keepers)
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)
        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return '\n'.join(result)