import unittest
import main

class TestMain(unittest.TestCase):

    def test_suma_cinco_uno(self):
        test_parameter = 1
        result = main.suma_cinco(test_parameter)
        self.assertEqual(result, 6)

    def test_suma_cinco_dos(self):
        test_parameter = 2
        result = main.suma_cinco(test_parameter)
        self.assertEqual(result, 7)

#unittest.main()
        
if __name__ == '__main__':
    unittest.main()