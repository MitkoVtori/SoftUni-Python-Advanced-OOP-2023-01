from unittest import TestCase, main

# from car import Car


class TestGunitSquad(TestCase):

    def setUp(self):
        self.car = Car("KR", "CHEVY", 5, 51)

    def test_successful_initialization(self):
        self.assertEqual("KR", self.car.make)
        self.assertEqual("CHEVY", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(51, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_unsuccessful_make_attribute_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_unsuccessful_model_attribute_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_unsuccessful_fuel_consumption_attribute_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_unsuccessful_fuel_capacity_attribute_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_unsuccessful_fuel_amount_attribute_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_unsuccessful_refuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_successful_refuel(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_successful_refuel_with_over_the_limit(self):
        amount = 1000
        self.car.refuel(amount)
        self.assertTrue(amount > self.car.fuel_capacity)
        self.assertEqual(51, self.car.fuel_capacity)

    def test_unsuccessful_drive_raise_exception(self):
        distance = 1000
        with self.assertRaises(Exception) as ex:
            self.car.drive(distance)

        self.assertTrue(distance > self.car.fuel_amount)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_successful_drive(self):
        self.car.fuel_amount = 51
        self.car.drive(100)
        self.assertEqual(46, self.car.fuel_amount)


if __name__ == "__main__":
    main()
