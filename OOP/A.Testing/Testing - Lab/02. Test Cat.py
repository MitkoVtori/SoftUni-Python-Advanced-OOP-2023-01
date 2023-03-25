from unittest import TestCase, main
# from cat import Cat


class CatTests(TestCase):

    def setUp(self):
        self.cat = Cat("Citty")

    def test_successful_initial(self):
        self.assertEqual("Citty", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_unsuccessful_eat_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_if_cat_size_increases_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)
        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)

    def test_unsuccessful_sleep_not_fed_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == '__main__':
    main()
