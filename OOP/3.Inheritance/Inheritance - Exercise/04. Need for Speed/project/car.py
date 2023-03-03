from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3
    fuel_consumption = 3

    def drive(self, kilometers):
        if self.fuel - (kilometers * Car.fuel_consumption) >= 0:
            self.fuel -= (kilometers * Car.fuel_consumption)
