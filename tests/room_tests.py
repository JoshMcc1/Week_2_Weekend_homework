import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song
import pdb
from classes.drink import Drink


from classes.bar_tab import BarTab


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("vodka", 4.00)
        self.bar_tab_1 = BarTab(1, 0, 0)
        self.room_1 = Room(1, 3, 15.00, self.bar_tab_1)
        self.song_1 = Song("Ants Marching", "Dave Matthews Band")
        self.song_2 = Song("son of A Preacher Man", "Dusty Springfield")
        self.song_3 = Song("Rammstein", "Du Hast")
        self.guest_1 = Guest("Jim", self.song_1, 9.00)
        self.guest_2 = Guest("Pam", self.song_1, 500.00)
        self.guest_3 = Guest("Lesly", self.song_2, 70.50)
        self.guest_4 = Guest("Obi Wan", self.song_1, 500.00)
        self.guest_5 = Guest("Maul", self.song_3, 35.00)

    def test_check_in_guest_pass(self):
        self.room_1.check_in(self.guest_2)
        self.assertEqual(1, len(self.room_1.guests))

    def test_check_in_guest_fail_not_enough_funds_in_wallet(self):
        self.assertEqual(
            "Guest does not have enough funds", self.room_1.check_in(self.guest_1)
        )

    def test_check_in_guest_fail_room_at_capicity(self):
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_4)
        self.assertEqual(
            "Cannot add more guests, room is at capcity",
            self.room_1.check_in(self.guest_5),
        )

    def test_check_out_guest_pass(self):
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(self.guest_3)
        self.room_1.check_out(self.guest_3)
        self.assertEqual(1, len(self.room_1.guests))

    def test_check_out_guest_fail_empty_list(self):
        self.assertEqual(
            "No guests currently in room to remove", self.room_1.check_out(self.guest_3)
        )

    def test_check_out_guest_fail_guest_has_not_been_added_to_list(self):
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(self.guest_3)
        self.assertEqual(
            "Guest has not been added to the current room",
            self.room_1.check_out(self.guest_1),
        )

    def test_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))

    def test_remove_song_pass(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_2)
        self.room_1.add_song(self.song_3)
        self.room_1.remove_song(self.song_1)
        self.assertEqual(2, len(self.room_1.songs))

    def test_remove_song_fail_no_songs_in_list(self):
        self.assertEqual(
            "No songs currently in room to remove", self.room_1.remove_song(self.song_1)
        )

    def test_remove_song_fail_song_has_not_been_added_to_list(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_2)
        self.assertEqual(
            "Song has not been added to the current room",
            self.room_1.remove_song(self.song_3),
        )

    def test_collect_fee_pass(self):
        self.room_1.collect_fee(self.guest_2)
        self.assertEqual(15, self.room_1.bar_tab.total_entry_fee)

    def test_collect_fee_fail(self):
        collect_fee_check = self.room_1.collect_fee(self.guest_1)
        self.assertEqual(False, collect_fee_check)

    def test_buy_drink(self):
        self.bar_tab_1.add_drink_to_list(self.drink_1)
        self.room_1.buy_drink(self.drink_1)
        self.assertEqual(4.00, self.bar_tab_1.drink_total)

    def test_entry_fee_total(self):
        self.room_1.check_in(self.guest_2)
        self.room_1.check_in(self.guest_3)
        self.room_1.check_in(self.guest_4)
        self.assertEqual(45.00, self.bar_tab_1.total_entry_fee)
