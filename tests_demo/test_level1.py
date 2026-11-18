import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    # ARRANGE, ACT and ASSERT <- General template

    def test_sum(self):
        # ARRANGE
        testCal = Calculator(8,2)
        # ACT & ASSERT
        self.assertEqual(testCal.get_sum(), 10, "The sum is wrong")

    # WRITE THE REMAINING TESTS FOR -, * and /

if __name__ == "__main__":
    unittest.main()
