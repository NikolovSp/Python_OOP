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

# all setters tests work, left with methods testing


if __name__ == '__main__':
    main()
