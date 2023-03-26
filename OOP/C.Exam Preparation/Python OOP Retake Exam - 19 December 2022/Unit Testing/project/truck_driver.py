from typing import Dict


class TruckDriver:
    def __init__(self, name: str, money_per_mile: float):
        self.name = name
        self.money_per_mile = money_per_mile
        self.available_cargos: Dict[str, int] = {}
        self.earned_money: float = 0
        self.miles: int = 0

    @property
    def earned_money(self):
        return self.__earned_money

    @earned_money.setter
    def earned_money(self, value):
        if value < 0:
            raise ValueError(f"{self.name} went bankrupt.")

        self.__earned_money = value

    def add_cargo_offer(self, cargo_location: str, cargo_miles: int):
        if cargo_location in self.available_cargos:
            raise Exception("Cargo offer is already added.")

        self.available_cargos[cargo_location] = cargo_miles

        return f"Cargo for {cargo_miles} to {cargo_location} was added as an offer."

    def drive_best_cargo_offer(self):
        try:
            cargo_location = max(self.available_cargos, key=self.available_cargos.get)
            cargo_miles = self.available_cargos[cargo_location]
        except ValueError:
            return "There are no offers available."

        self.earned_money += (cargo_miles * self.money_per_mile)
        self.miles += cargo_miles
        self.check_for_activities(cargo_miles)

        return f"{self.name} is driving {cargo_miles} to {cargo_location}."

    def check_for_activities(self, miles):
        for mile in range(1, miles + 1):
            self.eat(mile)
            self.sleep(mile)
            self.pump_gas(mile)
            self.repair_truck(mile)

    def eat(self, mile):
        if mile % 250 == 0:
            self.earned_money -= 20

    def sleep(self, mile):
        if mile % 1000 == 0:
            self.earned_money -= 45

    def pump_gas(self, mile):
        if mile % 1500 == 0:
            self.earned_money -= 500

    def repair_truck(self, mile):
        if mile % 10000 == 0:
            self.earned_money -= 7500

    def __repr__(self):
        return f"{self.name} has {self.miles} miles behind his back."
