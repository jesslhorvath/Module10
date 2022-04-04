"""
Programs: tests.py, student_objects.py, student.py
Author: Jessie Horvath
Modified: 04/04/2022

The purpose of these programs is to test a student class in various ways, 
including entering arguments that are not valid or out of range.
"""

import unittest
from student import Student as stu


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = stu('Pan', 'Peter', 'Biology')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Pan')
        self.assertEqual(self.student.first_name, 'Peter')
        self.assertEqual(self.student.major, 'Biology')

    def test_object_created_all_attributes(self):
        student = stu('Pan', 'Peter', 'Biology', 3.50)
        assert student.last_name == 'Pan'
        assert student.first_name == 'Peter'
        assert student.major == 'Biology'
        assert student.gpa == 3.50

    def test_student_str(self):
        assert self.student.__str__()

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = stu('123', 'Peter', 'Biology')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = stu('Pan', '123', 'Biology')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = stu('Pan', 'Peter', '123')
    
    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = stu('Pan', 'Peter', 'Biology', 'abc')

    def test_gpa_out_of_range(self):
        with self.assertRaises(ValueError):
            p = stu('Pan', 'Peter', 'Biology', 5.0)

if __name__ == '__main__':
    unittest.main()