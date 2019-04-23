import unittest
from interfaz_parcial import interfaz_decimal_hexa

class TestInterfazFactorial(unittest.TestCase):
    def test1_interfaz_parcial(self):
       result=interfaz_decimal_hexa(5)
       self.assertEqual(result, '5')

    def test2_interfaz_parcial(self):
       result=interfaz_decimal_hexa('hola')
       self.assertEqual(result, 'Disculpe, solo acepto numeros')

    def test3_interfaz_parcial(self):
       result=interfaz_decimal_hexa('')
       self.assertEqual(result, 'Disculpe, solo acepto numeros')

if __name__ == '__main__':
   unittest.main()