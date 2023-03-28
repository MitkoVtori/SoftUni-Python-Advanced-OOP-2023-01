from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(150.50, 200)

    def test_successful_initialization(self):
        self.assertEqual(150.50, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_unsuccessful_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(200)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_successful_drive(self):
        self.vehicle.drive(10)
        result = 150.50 - 12.5
        self.assertEqual(result, self.vehicle.fuel)

    def test_unsuccessful_refuel_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(3)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_successful_refuel(self):
        self.vehicle.capacity = self.vehicle.fuel * 2
        self.vehicle.refuel(50)
        self.assertEqual(200.50, self.vehicle.fuel)

    def test_str_method_successful_string_return(self):
        wanted_result = f"The vehicle has 200 " \
                        f"horse power with 150.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(wanted_result, str(self.vehicle))


if __name__ == '__main__':
    main()
