"""
Ćwiczymy działanie testowania klas.
"""
import unittest


class TestClass(unittest.TestCase):
    def test_class_1(self):
        self.assertTrue(True, 'Prawda jest prawdą')

    def test_class_2(self):
        self.assertFalse(False, 'Fałsz jest fałszem')

    def test_class_3(self):
        self.assertEqual('3.9'.split('.'), ['3', '9'], 'Czy dobrze użyłeś metody split?')

    def test_class_4(self):
        self.assertEqual('#'.join(['sport', 'gym']), 'sport#gym', 'Czy dobrze użyłeś metody join?')

    def test_class_5(self):
        self.assertTrue('apple'.islower())
