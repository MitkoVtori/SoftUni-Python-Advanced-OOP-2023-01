from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    def drive(self, kilometers):
        if self.fuel - (kilometers * Motorcycle.fuel_consumption) >= 0:
            self.fuel -= (kilometers * Motorcycle.fuel_consumption)
