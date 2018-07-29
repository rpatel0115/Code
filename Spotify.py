import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ["SPOTIPY_CLIENT_ID"] = ""
os.environ["SPOTIPY_CLIENT_SECRET"] = ""
username = "rpatel.0115"
# username = "samitpatel2005"
playlist_name = "🔥🔥Lititest🔥🔥"

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

