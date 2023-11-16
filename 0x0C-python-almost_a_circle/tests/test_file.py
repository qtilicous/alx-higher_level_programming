#!/usr/bin/python3
"""
test_my_module.test_module_file

Unit tests for the my_module.module_file module.
"""

import unittest
import io

from my_module.module_file import my_function, MyClass


class TestMyFunction(unittest.TestCase):
    def test_my_function(self):
        """
        Test my_function.

        It checks if the function prints the correct message.
        """
        # Redirect stdout to capture the print statement
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
        as mock_stdout:
            my_function()
            printed_message = mock_stdout.getvalue().strip()

        self.assertEqual(printed_message, "Hello from my_function!")


class TestMyClass(unittest.TestCase):
    def test_my_method(self):
        """
        Test MyClass.my_method.

        It checks if the method prints the correct message.
        """
        # Redirect stdout to capture the print statement
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
        as mock_stdout:
            instance = MyClass()
            instance.my_method()
            printed_message = mock_stdout.getvalue().strip()

        self.assertEqual(printed_message, "Hello from MyClass.my_method!")


if __name__ == '__main__':
    unittest.main()
