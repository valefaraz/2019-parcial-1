import unittest
from parcial import decimal_a_hexa

class TestDecimal(unittest.TestCase):
    def test_decimal_a_hexa1(self):
        decimal_hexa = decimal_a_hexa(5)
        self.assertEqual(decimal_hexa, '5')

    def test_decimal_a_hexa2(self):
        decimal_hexa = decimal_a_hexa(6)
        self.assertEqual(decimal_hexa, '6')

    def test_decimal_a_hexa3(self):
        decimal_hexa = decimal_a_hexa(7)
        self.assertEqual(decimal_hexa, '7')
    
    def test_decimal_a_hexa4(self):
        decimal_hexa = decimal_a_hexa(8)
        self.assertEqual(decimal_hexa,'8')
    
    def test_decimal_a_hexa5(self):
        decimal_hexa = decimal_a_hexa(9)
        self.assertEqual(decimal_hexa, '9')

    def test_decimal_a_hexa6(self):
        decimal_hexa = decimal_a_hexa(10)
        self.assertEqual(decimal_hexa, 'A')

    def test_decimal_a_hexa7(self):
        decimal_hexa = decimal_a_hexa(17)
        self.assertEqual(decimal_hexa, '11')

    def test_decimal_a_hexa8(self):
        decimal_hexa = decimal_a_hexa(16)
        self.assertEqual(decimal_hexa, '10')

    def test_decimal_a_hexa9(self):
        decimal_hexa = decimal_a_hexa(4095)
        self.assertEqual(decimal_hexa, '4D2')

    def test_decimal_a_hexa10(self):
        decimal_hexa = decimal_a_hexa(234)
        self.assertEqual(decimal_hexa, 'EA')


if __name__ == '__main__':
    unittest.main()