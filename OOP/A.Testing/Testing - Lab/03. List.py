from unittest import TestCase, main

# from list import IntegerList


class TestGunitSquad(TestCase):

    def setUp(self):
        self.list = IntegerList(1, 2, 3, "top", 2.2, False, ())

    def test_successful_initial(self):
        self.assertEqual([1, 2, 3], self.list._IntegerList__data)

    def test_successful_get_data(self):
        self.assertEqual([1, 2, 3], self.list.get_data())

    def test_unsuccessful_add_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.add("TOP THAT")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_successful_add_to_list(self):
        self.list.add(66)
        self.assertEqual([1, 2, 3, 66], self.list.get_data())
        # self.assertEqual([1,2,3,66], self.list._IntegerList__data)

    def test_unsuccessful_remove_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.remove_index(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_successful_remove_index_from_list(self):
        result = self.list.remove_index(0)
        self.assertEqual(1, result)
        self.assertEqual([2, 3], self.list._IntegerList__data)

    def test_unsuccessful_get_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.get(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_successful_get_item_from_list_by_index(self):
        result = self.list.get(0)

        self.assertEqual(1, result)
        self.assertEqual(1, self.list._IntegerList__data[0])

    def test_unsuccessful_insert_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(3, 4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_unsuccessful_insert_with_wrong_element_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, "1")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_successful_insert_element_in_list(self):
        self.list.insert(0, 10)

        self.assertEqual([10, 1, 2, 3], self.list._IntegerList__data)

    def test_successful_get_biggest_element_in_list(self):
        result = self.list.get_biggest()
        self.assertEqual(3, result)

    def test_successful_get_index_element_in_list(self):
        result = self.list.get_index(3)
        self.assertEqual(2, result)


if __name__ == "__main__":
    main()
