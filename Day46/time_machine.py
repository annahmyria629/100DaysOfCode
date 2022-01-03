from songs_scrapping import Songs
from spotify import Spotify
from utils import validate_date


if __name__ == '__main__':
    date = "2000/08/12"
    # date = input("Enter date in format yyyy-mm-dd:")
    songs = Songs(validate_date(date))
    songs_list = songs.scrap_songs()
    spotify = Spotify()
    playlist = spotify.create_playlist(f"The Hot 100 Billboard {validate_date(date)}")
    songs_uri_list = []
    no_such_songs_list = []
    for a, b in songs_list:
        b = b.replace(" Featuring ", ", ")
        t = spotify.find_song_uri(a, b)
        if t:
            songs_uri_list.append(t)
        else:
            no_such_songs_list.append((a, b))

    v = spotify.add_song_to_playlist(playlist_id=playlist, tracks_list=songs_uri_list)
    print("-"*100)
    print("No such songs:")
    print(*no_such_songs_list, sep="\n")
    print("-"*100)
    print("Done")
