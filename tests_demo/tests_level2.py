import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        # ARRANGE - Create and arrange your test data
        self.calc = Calculator(8,2)
        self.calc2 = Calculator(9,0)

    def test_sum(self):
        self.assertEqual(self.calc.get_sum(), 10, "The sum is wrong")

    def test_quotient(self):
        self.assertEqual(self.calc2.get_quotient(), 0, "The sum is wrong, it should give 0 due to division by 0")
    
    def tearDown(self):
        #Typically where you destroy assets you no longer need - Optional
        pass
        


if __name__ == "__main__":
    unittest.main()
