from unittest import TestCase
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("Kostadin", 1.40)

    def test_init(self):
        self.assertEqual(self.driver.name, "Kostadin")
        self.assertEqual(self.driver.money_per_mile, 1.40)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_valid(self):
        result = self.driver.add_cargo_offer("California", 2000)

        self.assertEqual(result, f"Cargo for 2000 to California was added as an offer.")
        self.assertEqual(self.driver.available_cargos, {"California": 2000})

    def test_add_cargo_invalid(self):
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("California", 2000)

        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_drive_best_cargo_offer_valid(self):
        self.driver.add_cargo_offer("California", 2000)
        self.driver.add_cargo_offer("Los Angeles", 20000)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(result, f"{self.driver.name} is driving 20000 to Los Angeles.")
        self.assertEqual(self.driver.earned_money, 4000)
        self.assertEqual(self.driver.miles, 20000)

    def test_drive_best_cargo_invalid(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_eat(self):
        self.driver.earned_money = 100

        self.driver.eat(250)
        self.driver.eat(500)

        self.assertEqual(self.driver.earned_money, 60)

    def test_sleep(self):
        self.driver.earned_money = 100

        self.driver.sleep(1000)
        self.driver.sleep(2000)

        self.assertEqual(self.driver.earned_money, 10)

    def test_pump_gas(self):
        self.driver.earned_money = 2000

        self.driver.pump_gas(1500)
        self.driver.pump_gas(3000)

        self.assertEqual(self.driver.earned_money, 1000)

    def repair_truck(self):
        self.driver.earned_money = 16000

        self.driver.repair_truck(10000)
        self.driver.repair_truck(20000)

        self.assertEqual(self.driver.earned_money, 1000)

    def test_repr(self):
        self.assertEqual(str(self.driver), "Kostadin has 0 miles behind his back.")
