from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink


class Room:
    def __init__(self, room_num, capacity, entry_fee, bar_tab) -> None:
        self.room_num = room_num
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.bar_tab = bar_tab
        self.guests = []
        self.songs = []

    def check_in(self, guest_to_check_in):
        if self.collect_fee(guest_to_check_in):
            if len(self.guests) < self.capacity:
                self.guests.append(guest_to_check_in)
            else:
                return "Cannot add more guests, room is at capcity"
        else:
            return "Guest does not have enough funds"

    def check_out(self, guest_to_check_out):
        if len(self.guests) > 0:
            if self.guests.__contains__(guest_to_check_out):
                self.guests.remove(guest_to_check_out)
            else:
                return "Guest has not been added to the current room"
        else:
            return "No guests currently in room to remove"

    def add_song(self, song_to_add):
        self.songs.append(song_to_add)

    def remove_song(self, song_to_remove):
        if len(self.songs) > 0:
            if self.songs.__contains__(song_to_remove):
                self.songs.remove(song_to_remove)
            else:
                return "Song has not been added to the current room"
        else:
            return "No songs currently in room to remove"

    def collect_fee(self, guest_to_pay):
        if guest_to_pay.pay_entry_fee(self.entry_fee):
            self.bar_tab.total_entry_fee += self.entry_fee
            return True
        else:
            return False

    def buy_drink(self, drink):
        self.bar_tab.drink_total += drink.price
