import unittest
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        print('Iniciando las pruebas automaitcas del unittest para la funcion suma_cinco()')

    def test_suma_cinco_uno(self):
        test_parameter = 5
        result = main.suma_cinco(test_parameter)
        self.assertEqual(result, 10)
        print('Validando 5  + 10, si es correcto')

    def test_suma_cinco_dos(self):
        test_parameter = 'string'
        result = main.suma_cinco(test_parameter)
        self.assertIsInstance(result, ValueError)
        print('Validando test_suma_cinco_dos')

    def test_suma_cinco_tres(self):
        test_parameter = None
        result = main.suma_cinco(test_parameter)
        self.assertEqual(result, "Por favor ingresa un numero")
        print('Validando test_suma_cinco_tres')
    
    def test_suma_cinco_cuatro(self):
        test_parameter = ''
        result = main.suma_cinco(test_parameter)
        self.assertEqual(result, "Por favor ingresa un numero")
        print('Validando test_suma_cinco_cuatro')



unittest.main()
'''
if __name__ == '__main__':
    unittest.main()
'''