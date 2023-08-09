import unittest
from main import calculate_factorial

class TestFactorial(unittest.TestCase):
    def test_calculate_factorial(self):
        # Arrange
        input_num = 5
        expected_output = 120
        
        # Act
        result = calculate_factorial(input_num)
        
        # Assert
        self.assertEqual(expected_output, result)

if __name__ == '__main__':
    unittest.main()