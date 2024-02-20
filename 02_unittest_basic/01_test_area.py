"""
Pierwszy test jednostkowy.
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
    def test_area(self):
        self.assertEqual(area(4, 5), 20, 'Prostokąt 4 x 5 ma pole 20')

    def test_area_incorrect_type_should_raise_error(self):
        self.assertRaises(TypeError, area, '4', 5)
        self.assertRaises(TypeError, area, 4, '5')

    def test_area_negative_value_should_raise_error(self):
        self.assertRaises(ValueError, area, -4, 5)
        self.assertRaises(ValueError, area, 4, -5)



    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-4, 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)