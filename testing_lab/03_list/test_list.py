from unittest import TestCase, main
from integer_list import IntegerList


class ListTest(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(
            1,
            '55',
            2,
            5.5,
            False,
            5
        )

    def test_correct_input_data(self):
        self.assertEqual([1, 2, 5], self.integer_list.get_data())

    def test_add_element_not_integer_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(8.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_element_if_element_is_integer(self):
        expected_result = self.integer_list.get_data() + [8]
        self.integer_list.add(8)

        self.assertEqual(expected_result, self.integer_list.get_data())

    def test_remove_by_index_with_index_out_of_range_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(100)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_element_by_index_and_return_removed_element(self):
        expected_element = 2
        actual_element = self.integer_list.remove_index(1)

        self.assertEqual([1, 5], self.integer_list.get_data())
        self.assertEqual(expected_element, actual_element)

    def test_element_by_index_out_of_range_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(100)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_element_by_index_but_not_remove_from_list(self):
        element_taken = self.integer_list.get(1)
        self.assertEqual(2, element_taken)
        self.assertEqual([1, 2, 5], self.integer_list.get_data())

    def test_index_out_of_range_when_adding_element(self):
        with self.assertRaises(IndexError)as ie:
            self.integer_list.insert(100, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_element_is_integer_when_adding_element(self):
        with self.assertRaises(ValueError)as ve:
            self.integer_list.insert(2, 5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_element_when_integer_and_valid_index(self):
        expected_list = [1 ,2 , 8, 5]
        self.integer_list.insert(len(self.integer_list.get_data()) - 1, 8)
        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_get_biggest_element(self):
        self.assertEqual(5, self.integer_list.get_biggest())

    def test_get_index_of_element(self):
        element = 2
        index = 1
        self.assertEqual(index, self.integer_list.get_index(element))


if __name__ == '__main__':
    main()
