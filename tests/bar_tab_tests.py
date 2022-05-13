import unittest
from classes.bar_tab import BarTab
from classes.drink import Drink


class TestBarTab(unittest.TestCase):
    def setUp(self):
        self.bar_tab_1 = BarTab(1, 0, 0)
        self.drink_1 = Drink("vodka", 4.00)
        self.drink_2 = Drink("Guinness", 3.80)

    def test_add_drink_to_list(self):
        self.bar_tab_1.add_drink_to_list(self.drink_1)
        self.assertEqual(1, len(self.bar_tab_1.drinks))

    def test_remove_drink_from_list_pass(self):
        self.bar_tab_1.add_drink_to_list(self.drink_1)
        self.bar_tab_1.add_drink_to_list(self.drink_2)
        self.bar_tab_1.remove_drink_from_list(self.drink_2)
        self.assertEqual(1, len(self.bar_tab_1.drinks))

    def test_remove_drink_from_list_fail_empty_list(self):
        self.assertEqual(
            "No drinks currently in list to remove",
            self.bar_tab_1.remove_drink_from_list(self.drink_1),
        )

    def test_remove_drink_from_list_fail_drink_not_in_list(self):
        self.bar_tab_1.add_drink_to_list(self.drink_1)
        self.assertEqual(
            "Drink is not in list", self.bar_tab_1.remove_drink_from_list(self.drink_2)
        )
