import unittest
from classes.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Vodka", 4.00)

    def test_drink_has_name(self):
        self.assertEqual("Vodka", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(4.00, self.drink_1.price)
