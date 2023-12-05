from unittest import TestCase, main
from worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker('Pesho', 100, 10)

    def test_correct_input(self):
        self.assertEqual('Pesho', self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_worker_has_energy_to_work_raise_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_worker_has_energy_and_increase_money_decrease_energy(self):
        expected_money = self.worker.salary
        expected_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_rest_increases_energy(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_str_return_of_data(self):
        expected_str = f'{self.worker.name} has saved {self.worker.money} money.'

        self.assertEqual(expected_str, self.worker.get_info())


if __name__ == '__main__':
    main()
