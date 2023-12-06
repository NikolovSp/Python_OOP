from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.bmw = Vehicle(100, 500)

    def test_correct_init(self):
        self.assertEqual(100, self.bmw.fuel)
        self.assertEqual(100, self.bmw.capacity)
        self.assertEqual(500, self.bmw.horse_power)
        self.assertEqual(1.25, self.bmw.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(1.25, self.bmw.fuel_consumption)

    def test_if_drive_more_than_given_fuel_raise_exception(self):
        distance = 100
        # fuel_needed = distance * self.bmw.fuel_consumption
        with self.assertRaises(Exception) as ex:
            self.bmw.drive(distance)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_if_enough_fuel_reduce_fuel(self):
        distance = 20
        self.bmw.drive(distance)
        self.assertEqual(75, self.bmw.fuel)

    def test_refuel_if_fuel_is_more_than_capacity_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bmw.refuel(150)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_when_there_is_more_capacity(self):
        self.bmw.fuel = 10
        self.bmw.refuel(40)
        self.assertEqual(50, self.bmw.fuel)

    def test_str_return_of_the_data(self):
        expected_result = f"The vehicle has {self.bmw.horse_power} " \
               f"horse power with {self.bmw.fuel} fuel left and {self.bmw.fuel_consumption} fuel consumption"

        self.assertEqual(expected_result, self.bmw.__str__())


if __name__ == '__main__':
    main()
