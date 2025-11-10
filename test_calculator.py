import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_add1(self):
        self.assertEqual(self.calc.add(-2, 0), -2)
    def test_add2(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(6, 4), 2)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_divided1(self):
        self.assertEqual(self.calc.divide(100, 5), 20)
    def test_divided2(self):
        self.assertEqual(self.calc.divide(300, 2), 150)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(18, 3), 0)

    

if __name__ == '__main__':
    calc = unittest.main()
   