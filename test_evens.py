import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase): #to make use of unittest functionality, we need to inherit from the unittest.TestCase class
    # def test_function_returns_True(self):
    #     self.assertTrue(even_number_of_evens)
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):  
        self.assertEqual(even_number_of_evens([]), False) #Test if False is returned if an empty list is passed in. Empty list passed in as argument, assertEqual checks if it is equal to nothing, then returns False
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


unittest.main()