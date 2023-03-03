from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
    fuel_consumption = 10

    def drive(self, kilometers):
        if self.fuel - (kilometers * SportCar.fuel_consumption) >= 0:
            self.fuel -= (kilometers * SportCar.fuel_consumption)
