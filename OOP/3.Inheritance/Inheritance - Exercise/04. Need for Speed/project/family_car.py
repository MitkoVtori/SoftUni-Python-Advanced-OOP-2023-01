from project.car import Car


class FamilyCar(Car):
    def drive(self, kilometers):
        if self.fuel - (kilometers * FamilyCar.fuel_consumption) >= 0:
            self.fuel -= (kilometers * FamilyCar.fuel_consumption)
