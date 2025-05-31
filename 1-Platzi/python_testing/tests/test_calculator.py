import unittest
import sys
import os

# Agregar el directorio padre al path para que Python pueda encontrar src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.calculator import sum, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_sum(self):
        assert sum(1, 2) == 3

    def test_subtract(self):
        assert subtract(5, 3) == 2

    def test_multiply(self):
        assert multiply(2, 3) == 6
        
    def test_divide(self):
        assert divide(6, 2) == 3
        with self.assertRaises(ValueError):
            divide(5, 0)
            
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)