from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.A = Student('A')
        self.B = Student('B', {'Python': ['n1', 'n2', 'n3'], 'JS': ['b1', 'b3']})

    def test_correct_init(self):
        self.assertEqual('A', self.A.name)
        self.assertEqual({}, self.A.courses)
        self.assertEqual({'Python': ['n1', 'n2', 'n3'], 'JS': ['b1', 'b3']}, self.B.courses)

    def test_adding_course_to_the_list_if_course_already_exists(self):
        result = self.B.enroll('JS', ['b2'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'Python': ['n1', 'n2', 'n3'], 'JS': ['b1', 'b3', 'b2']}, self.B.courses)

    def test_add_course_not_in_course_with_notes_Y(self):
        result = self.A.enroll('C++', ['c1', 'c2'], 'Y')

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'C++': ['c1', 'c2']}, self.A.courses)

    def test_add_course_not_in_course_with_notes_empty(self):
        result = self.A.enroll('C++', ['c1', 'c2'], '')

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'C++': ['c1', 'c2']}, self.A.courses)

    def test_add_course_when_not_in_dict_and_course_notes_are_in(self):
        result = self.A.enroll('C++', ['c1', 'c2'], 'Hi')
        self.assertEqual("Course has been added.", result)
        self.assertEqual({'C++': []}, self.A.courses)

    def test_add_notes_if_course_not_in_course_list_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.A.add_notes('C++', ['c1', 'c2'])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_to_already_existing_course_update_notes(self):
        result = self.B.add_notes('JS', 'b2')

        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'Python': ['n1', 'n2', 'n3'], 'JS': ['b1', 'b3', 'b2']}, self.B.courses)

    def test_remove_course_when_course_not_in_courses_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.A.leave_course('JS')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_remove_course_from_course_list_return_str(self):
        result = self.B.leave_course('Python')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({'JS': ['b1', 'b3']}, self.B.courses)


if __name__ == '__main__':
    main()
