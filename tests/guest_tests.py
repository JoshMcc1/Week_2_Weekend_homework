import unittest
from classes.song import Song
from classes.guest import Guest
from classes.room import Room
from classes.bar_tab import BarTab


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.bar_tab_1 = BarTab(1, 0, 0)
        self.song_1 = Song("Ants Marching", "Dave Matthew's Band")
        self.guest_1 = Guest("Ahsoka", self.song_1, 100.00)
        self.guest_2 = Guest("Jim", self.song_1, 8)
        self.room_1 = Room(1, 10, 15.00, self.bar_tab_1)

    def test_guest_pays_entry_fee_pass(self):
        pay_fee_check = self.guest_1.pay_entry_fee(self.room_1.entry_fee)
        self.assertEqual(True, pay_fee_check)

    def test_guest_pays_entry_fee_fail(self):
        pay_fee_check = self.guest_2.pay_entry_fee(self.room_1.entry_fee)
        self.assertEqual(False, pay_fee_check)

    def test_cheer(self):
        self.room_1.check_in(self.guest_1)
        self.room_1.add_song(self.song_1)
        self.assertEqual("Whoop Whoop!!!!", self.guest_1.cheer(self.room_1))
