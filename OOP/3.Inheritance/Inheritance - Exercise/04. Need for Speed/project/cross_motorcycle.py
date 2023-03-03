from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    def drive(self, kilometers):
        if self.fuel - (kilometers * CrossMotorcycle.fuel_consumption) >= 0:
            self.fuel -= (kilometers * CrossMotorcycle.fuel_consumption)

