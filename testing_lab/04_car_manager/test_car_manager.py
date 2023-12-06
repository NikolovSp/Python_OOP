from unittest import TestCase, main
from car_manager import Car


class CarManagerTest(TestCase):
    def setUp(self):
        self.car = Car('Toyota', 'LC200', 10, 100)

    def test_correct_innit(self):
        self.assertEqual('Toyota', self.car.make)
        self.assertEqual('LC200', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_input_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car('', 'LC200', 10, 100)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Toyota', '', 10, 100)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_cannot_be_negative(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Toyota', 'LC200', 0, 100)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_cannot_be_negative(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Toyota', 'LC200', 10, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_added_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))


    def test_refuel_if_fuel_given_is_negative_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-5)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_more_than_fuel_capacity(self):

        self.car.refuel(140)
        self.assertEqual(100, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel_reduce_fuel_amount(self):
        self.car.fuel_amount = 50
        self.car.drive(100)

        self.assertEqual(40, self.car.fuel_amount)


if __name__ == '__main__':
    main()
