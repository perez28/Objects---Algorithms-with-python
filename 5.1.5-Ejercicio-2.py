class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
artis =Artist("Taylor Swift", "Big Machine Records, LLC")
song_1 = Song ("You Belong With Me","Fearless",2008,artis)
song_2 = Song ("All Too Well","Red",2012,artis)
song_3 = Song ("Up We Go","Midnight Machines",2016,Artist("LiGHTS", "Warner Bros. Records Inc."))
