import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Ants Marching", "Dave Matthew's Band")

    def test_song_has_title(self):
        self.assertEqual("Ants Marching", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Dave Matthew's Band", self.song_1.artist)
