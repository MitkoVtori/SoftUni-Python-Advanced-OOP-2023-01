from unittest import TestCase, main
# from worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("test", 15, 25)


    def test_if_person_is_initialized_successfully(self):
        self.assertEqual("test", self.worker.name)
        self.assertEqual(15, self.worker.salary)
        self.assertEqual(25, self.worker.energy)
        self.assertEqual(0, self.worker.money)


    def test_successful_work(self):
        self.worker.work()
        self.assertEqual(15, self.worker.money)
        self.assertEqual(24, self.worker.energy)

    def test_unsuccessful_work_not_enough_energy_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_rest_method_increases_the_energy(self):
        self.worker.rest()
        self.assertEqual(26, self.worker.energy)

    def test_get_info_string_return(self):
        self.assertEqual(f'test has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
