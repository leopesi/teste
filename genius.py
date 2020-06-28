from lyricsgenius import Genius

def get_popularity_songs(artist_name: str, max_songs: int, sort="popularity"):
    genius = Genius("WLSp00664-lpegmyI7i4KYmZ5UA_yYf55lNo7auQ6PuBEw3ziIvOkLL8ABZqeNl7")
    artist = genius.search_artist(artist_name, max_songs=max_songs, sort=sort)
    return artist.songs
