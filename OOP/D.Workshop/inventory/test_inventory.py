from unittest import TestCase, main
from inventory import Inventory


class TestInventory(TestCase):

    def setUp(self) -> None:
        self.inventory = Inventory(1, 2, 3, 4, 5, "Glass", True)

    def test_string_return(self):
        self.assertEqual("[1, 2, 3, 4, 5, \'Glass\', True]", str(self.inventory))

    def test_unsuccessful_indexing(self):
        with self.assertRaises(IndexError) as ie:
            result = self.inventory[67]

        self.assertEqual("Index out of range!", str(ie.exception))

    def test_successful_indexing(self):
        result = self.inventory[-3]
        result2 = self.inventory[0]
        result3 = self.inventory[4]

        self.assertEqual(5, result)
        self.assertEqual(1, result2)
        self.assertEqual(5, result3)

    def test_append(self):
        self.inventory.append([1, 2, 3])
        self.assertEqual([1, 2, 3], self.inventory[-1])

    def test_extend(self):
        self.inventory.extend([1, 2, 3])
        self.assertEqual(2, self.inventory[-2])

    def test_insert(self):
        self.inventory.insert(0, "G")
        self.assertEqual("G", self.inventory[0])
        self.inventory.insert(-3, "J")
        self.assertEqual("J", self.inventory[-3])
        self.assertEqual("[\'G\', 1, 2, 3, 4, 5, \'J\', \'Glass\', True]", str(self.inventory))

    def test_add_first(self):
        self.inventory.add_first(9)
        self.assertEqual(9, self.inventory[0])

    def test_size(self):
        self.assertEqual(7, self.inventory.size())

    def test_remove(self):
        self.inventory.remove(-1)
        self.assertEqual("Glass", self.inventory[-1])
        self.assertEqual(6, self.inventory.size())

    def test_clear(self):
        self.inventory.clear()
        self.assertEqual('[]', str(self.inventory))

    def test_pop(self):
        result = self.inventory.pop()
        self.assertEqual(True, result)

    def test_index_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.inventory.index("Kiro")

        self.assertEqual("Value not found!", str(ve.exception))

    def test_index(self):
        result = self.inventory.index(1)
        self.assertEqual(0, result)

    def test_get(self):
        self.assertEqual(1, self.inventory.get(0))

    def test_count(self):
        self.assertEqual(0, self.inventory.count(Inventory))

    def test_reverse(self):
        self.inventory = Inventory(1, 2, 3)
        self.assertEqual("[3, 2, 1]", str(self.inventory.reverse()))

    def test_copy(self):
        inventory_copy = self.inventory.copy()
        self.assertEqual(str(inventory_copy), str(self.inventory))
        self.assertNotEqual(inventory_copy, self.inventory)

    def test_sum(self):
        self.assertEqual(21, self.inventory.sum())

    def test___dict__(self):
        self.inventory = Inventory(1)
        self.assertEqual({0: 1}, self.inventory.__dict__())


if __name__ == '__main__':
    main()
