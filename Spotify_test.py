import spotipy
import spotipy.util as util
from configparser import ConfigParser
import keys
parser = ConfigParser()
#Reads config.ini file for API keys
username = "rpatel.0115"


class User():

    def __init__(self):
        parser.read("config.ini")
        self.CLIENT_ID = keys.SPOTIFY_CLIENT_ID
        self.CLIENT_SECRET = keys.SPOTIFY_CLIENT_SECRET
        self.REDIRECT_URI = 'https://www.google.com/'

        self.SCOPE = "playlist-read-private playlist-modify-private playlist-read-collaborative playlist-modify-public" #Allows program to access/edit private and public playlists
        self.sp = self.getuser() #Creates Spotify Instance
        self.id = self.sp.me()['id'] #Gets ID of authenticating user

    def getuser(self):
        """Creates Spotify instance for Authenticating User"""
        token = self.getUserToken()
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        return sp

    def getfeatures(self, track):
        """Retrieves Audio features from Spotify API for a single track"""
        features = self.sp.audio_features(track)
        return features

    def getplaylist(self):

        """Retrieves all playlists from authenticating user, then allows user to select one"""

        results = self.sp.current_user_playlists()

        for i, item in enumerate(results['items']):

            print("{number} {name}".format(number=i, name=item['name'].encode('utf8'))) #Prints out the name of each playlist, preceded by a number

        choice = input("Please choose a playlist number: ")

        return results['items'][int(choice)]['id']

    def getsongs(self, playlist_id):

        """Gets all songs from a chosen playlist, returns a lsit of all song ids"""

        results = self.sp.user_playlist_tracks(self.id,playlist_id)

        tracks = results['items']

        song_ids = []

        while results['next']:

            results = self.sp.next(results)

            tracks.extend(results['items'])

        for song in tracks:

            song_ids.append(song['track']['id'])

        return song_ids

    def getUserToken(self):

        """Gets authentication token from user"""

        name = username

        token = util.prompt_for_user_token(username=name,scope=self.SCOPE, client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, redirect_uri=self.REDIRECT_URI)
        print(f"This is your token: {token}")
        return token



    # def sortSongs(self, songF, danceL, danceH, energyL, energyH, loudL, loudH, acousticL, acousticH,
    #
    # 	instrumentL, instrumentH, livenessL, livenessH, valenceL, valenceH):
    #
    # 	"""Returns True if all conditions are met. Conditions include: Danceability, Energy, Loudness, Acousticness, Instrumentalness, Liveness, and Valence"""
    #
    # 	if danceL <= songF['danceability'] <= danceH:
    #
    # 		if energyL <= songF['energy'] <= energyH:
    #
    # 			if loudL <= songF['loudness'] <= loudH:
    #
    # 				if acousticL <= songF['acousticness'] <= acousticH:
    #
    # 					if instrumentL <= songF['instrumentalness'] <= instrumentH:
    #
    # 						if livenessL <= songF['liveness'] <= livenessH:
    #
    # 							if valenceL <= songF['valence'] <= valenceH:
    #
    # 								return True

    # def getLimits(self):

        # """Asks user for the minimums and maximums for each condition, leaving a blank responistse will return the lowest or highest possible value. Then asks user to name the playlist"""
        #
        # danceL = float(raw_input("Danceability minimum (how suitable track is for dancing 0.0-1.0): ") or "0")
        #
        # danceH = float(raw_input("Danceability maximum: ") or "1")
        #
        # energyL = float(raw_input("Energy minimum (intensity, or speed of a track 0.0-1.0): ") or "0")
        #
        # energyH = float(raw_input("Energy maximum: ") or "1")
        #
        # loudL = float(raw_input("Loudness minimum (Overall loudness of a track in decibels -60-0): ") or "-60")
        #
        # loudH = float(raw_input("Loudness maximum: ") or "0")
        #
        # acousticL = float(raw_input("Acousticness minimum (measure of whether a track is acoustic 0.0-1): ") or "0")
        #
        # acousticH = float(raw_input("Acousticness maximum: ") or "1")
        #
        # instrumentL = float(raw_input("Instrumentalness minimum (Predicts whether track contains no vocals 0.0-1.0): ") or "0")
        #
        # instrumentH = float(raw_input("Instrumentalness maximum: ") or "1")
        #
        # livenessL = float(raw_input("Liveness minimum (Detects presence of audience 0.0-1.0): ") or "0")
        #
        # livenessH = float(raw_input("Liveness maximum: ") or "1")
        #
        # valenceL = float(raw_input("Valence minimum (Positivity measurement 0.0-1.0): ") or "0")
        #
        # valenceH = float(raw_input("Valence maximum: ") or "1")
        #
        # name = raw_input("Please name your playlist: ")
        #
        # return [danceL, danceH, energyL, energyH, loudL, loudH, acousticL, acousticH, instrumentL, instrumentH, livenessL, livenessH, valenceL, valenceH, name]
        #


    def createplaylist(self, title, tracks):

        """Creates a new playlist from all tracks that met conditions"""

        playlist = self.sp.user_playlist_create(self.id, title, False)

        for track in tracks:

            self.sp.user_playlist_add_tracks(self.id, playlist['id'], [track])

        print("Playlist Created")

    def main(self):
        playlist = "newest 2"
        self.sp.user_playlist_create(user=self.id, name=f'{playlist}', public=False)
        #
        # playlist = self.getPlaylist()
        #
        # songs = self.getSongs(playlist)
        #
        # newPlaylist = []
        #
        # pref = self.getLimits()
        #
        # for song_id in songs:
        #
        #     song = self.getFeatures([song_id])
        #
        #     if self.sortSongs(song[0], pref[0], pref[1], pref[2], pref[3], pref[4], pref[5], pref[6], pref[7], pref[8], pref[9], pref[10], pref[11], pref[12], pref[13]):
        #
        #         newPlaylist.append(song[0]['id'])
        #
        # self.createPlaylist(pref[14], newPlaylist)


if __name__ == "__main__":

    SpotifyUser = User()

    SpotifyUser.main()





