import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import List

scope = "playlist-modify-private playlist-modify-public"
client_id = "client_id"
client_secret = "client_secret"
redirect_uri = "http://example.com/"


class Spotify:
    # user_id: str = None

    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope))
        self.user_id = self.sp.current_user()["id"]

    def create_playlist(self, playlist_name: str, public: bool = True, description: str = "") -> str:
        # user_id = self.sp.current_user()["id"]
        playlists = self.sp.user_playlists(user=self.user_id)
        pl = [p for p in playlists["items"] if p["name"] == playlist_name]
        if not pl:
            res = self.sp.user_playlist_create(user=self.user_id, name=playlist_name, public=public, description=description)
            return res["id"]
        else:
            return pl[0]["id"]

    def find_song_uri(self, song_name: str, singer: str) -> str:
        s = self.sp.search(q=f"track:{song_name} artist:{singer}", type="track,artist")
        if s["tracks"]["items"]:
            return s["tracks"]["items"][0]["uri"]

    def add_song_to_playlist(self, playlist_id: str, tracks_list: List[str]):
        add = self.sp.playlist_add_items(playlist_id=playlist_id, items=tracks_list)
        return add

