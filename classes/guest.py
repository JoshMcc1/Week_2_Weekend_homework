class Guest:
    def __init__(self, name, fav_song, wallet):
        self.name = name
        self.fav_song = fav_song
        self.wallet = wallet

    def pay_entry_fee(self, entry_fee):
        if self.wallet >= entry_fee:
            return True
        else:
            return False

    def cheer(self, room):
        if room.songs.__contains__(self.fav_song):
            return "Whoop Whoop!!!!"
