from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENTS = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAMS = {"IndoorTeam": IndoorTeam, "OutdoorTeam": OutdoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if not value.isallnum():

            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENTS.keys():
            raise Exception("Invalid equipment type!")
        self.equipment.append(self.EQUIPMENTS[equipment_type])

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAMS:
            raise Exception("Invalid team type!")
        if len(self.teams) == self.capacity:

            return "Not enough tournament capacity."

        self.teams.append(self.TEAMS[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = next(e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type)
        team = next(t for t in self.teams if t.name == team_name)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        pass

    def increase_equipment_price(self, equipment_type: str):
        pass

    def play(self, team_name1: str, team_name2: str):
        pass
    
    def get_statistics(self):
        pass

