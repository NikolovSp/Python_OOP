from abc import ABC, abstractmethod
from math import floor
from typing import List

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: List[BaseEquipment] = []

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        price_of_equipment = sum([e.price for e in self.equipment])
        average_team_protection = sum([e.protection for e in self.equipment]) / len(self.equipment)
        return (f"Name: {self.name}\n"
                f"Country: {self.country}\n"
                f"Advantage: {self.advantage} points\n"
                f"Budget: {self.budget:.2f}EUR\n"
                f"Wins: {self.wins}\n"
                f"Total Equipment Price: {price_of_equipment:.2f}\n"
                f"Average Protection: {floor(average_team_protection)}")
