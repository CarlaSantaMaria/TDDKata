import unittest
from src.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornarNone(self):
        conjunto=Conjunto([])
        self.assertIsNone(conjunto.promedio())


if __name__ == '__main__':
    unittest.main()
