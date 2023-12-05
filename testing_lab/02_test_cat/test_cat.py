from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat('Pipi')

    def test_correct_data_input(self):
        self.assertEqual('Pipi', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_feed_cat_if_already_fed_raise_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_not_fed_increase_size(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_if_cat_fed_and_can_sleep(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_if_cat_not_fed_cannot_sleep_exception(self):
        self.cat.sleepy = False
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()
