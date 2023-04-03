from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_successful_initialization(self):
        shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(shelf, self.toy_store.toy_shelf)

    def test_add_toy_invalid_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("7", "Mark")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_already_in_shelf(self):
        self.toy_store.toy_shelf = {"A": "Mark"}

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Mark")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_shelf_already_taken(self):
        self.toy_store.toy_shelf["A"] = "Mark"

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "John")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_successful_add_toy(self):
        result = self.toy_store.add_toy("A", "Mark")
        shelf = {
            "A": "Mark",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(shelf, self.toy_store.toy_shelf)
        self.assertEqual(f"Toy:Mark placed successfully!", result)

    def test_remove_toy_shelf_not_in_shelf_keys(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("7", "Mark")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_name_not_in_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Mark")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_successful_remove_toy(self):
        self.toy_store.toy_shelf = {
            "A": "Mark",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        result = self.toy_store.remove_toy("A", "Mark")
        self.assertEqual(None, self.toy_store.toy_shelf["A"])
        self.assertEqual(f"Remove toy:Mark successfully!", result)


if __name__ == '__main__':
    main()
