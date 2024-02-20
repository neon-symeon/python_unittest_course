"""
Możliwe wyniki testu jednostkowego.
"""
import unittest


def area(width, height):
    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('Wartości muszą być liczbami.')

    if not (width > 0 and height > 0):
        raise ValueError('Wartości muszą być dodatnie.')

    return width * height


class TestArea(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(4, 5), 20, 'Prostokąt 4 x 5 ma pole 20')

    def test_area_2(self):
        self.assertEqual(area(4, 5), 21, 'Prostokąt 4 x 5 ma pole 20')

    def test_area_3(self):
        raise AssertionError('Błąd asercji')

    def test_area_4(self):
        raise TypeError('Błąd asercji')

