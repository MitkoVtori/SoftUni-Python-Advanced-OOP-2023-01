from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    fuel_consumption = 8

    def drive(self, kilometers):
        if self.fuel - (kilometers * RaceMotorcycle.fuel_consumption) >= 0:
            self.fuel -= (kilometers * RaceMotorcycle.fuel_consumption)
