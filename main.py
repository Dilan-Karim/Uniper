"""
This module is responsible for running the test suite for the Uniper coding interview.

The `run_test_suite` function loads the test cases from the respective test modules,
creates a test suite containing all the test cases, and executes the test suite.

Usage:
    - Call the `run_test_suite` function to run all the test cases.
"""

import unittest
import tests.exercise_1.test_resistor as test1
import tests.exercise_2.test_alt_list as test2
import tests.exercise_3.test_binary_search_tree as test3


def run_test_suite():
    """
    Runs the test suite containing all the test cases.

    This function loads the test cases from the respective test modules,
    creates a test suite containing all the test cases, and executes the test suite.

    Usage:
        - Call this function to run all the test cases.

    """
    # Load the test cases
    test_cases_1 = unittest.TestLoader().loadTestsFromTestCase(test1.TestResistor)
    test_cases_2 = unittest.TestLoader().loadTestsFromTestCase(test2.TestList)
    test_cases_3 = unittest.TestLoader().loadTestsFromTestCase(test3.TestBinarySearchTree)

    # Create a test suite containing all the test cases
    test_suite = unittest.TestSuite([test_cases_1, test_cases_2, test_cases_3])

    # Execute the test suite
    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    run_test_suite()
