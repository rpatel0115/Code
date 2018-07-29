import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import keys

os.environ["SPOTIPY_CLIENT_ID"] = keys.SPOTIFY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = keys.SPOTIFY_CLIENT_SECRET
username = "rpatel.0115"
# username = "samitpatel2005"
playlist_name = "🔥🔥Lititest🔥🔥"

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_playlist():
    playlists = sp.user_playlists(username)
    while playlists:
        for playlist in playlists['items']:
            if playlist_name == playlist['name']:
                return playlist
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None


def get_tracks(my_playlist):
    results = sp.user_playlist(username, my_playlist['id'],fields="tracks,next")
    tracks = results['tracks']
    for item in tracks['items']:
        track_info(track_item=item)
    while tracks['next']:
        tracks = sp.next(tracks)
        for item in tracks['items']:
            track_info(track_item=item)


def track_info(track_item):
    track = track_item['track']
    artist = track['artists'][0]['name']
    track_name = track['name']
    print(f"{artist}: {track_name}")


my_playlist = get_playlist()

print(my_playlist)
get_tracks(my_playlist=my_playlist)