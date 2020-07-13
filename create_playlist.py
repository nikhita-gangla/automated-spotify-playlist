import json
import requests # allows us to make http requests using python
import os
from exceptions import ResponseException

# spotify API information
from secrets import spotify_user_id, spotify_token

# youtube data api
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# youtube dl API
import youtube_dl

class CreatePlaylist:

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token
        self.youtube_client = self.get_youtube_client()
        self.all_song_info = {}

    # Step 1: Log into Youtube
    def get_youtube_client(self):
        """
        This method logs us into youtube.
        :return: youtube_client
        """

        """ Log Into Youtube, Copied from Youtube Data API """
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()

        # from the Youtube DATA API
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        return youtube_client


    # Step 2: Grab liked videos and create a dictionary of important song information
    def get_liked_videos(self):
        """
        This method retrieves our Youtube Liked videos and creates a dictionary of song information (track names and artists)
        using the youtube dl API. It stores them in the all_song_info object attribute.
        :return: None,
        """

        # This gets the liked details and stores all of our important information
        request = self.youtube_client.videos().list(
            part= "snippet,contentDetails,statistics",
            myRating="like"
        )
        response = request.execute()

        # loop through and collect each video item
        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url = "https://www.youtube.com/watch?v={}".format(item["id"])

            # use youtube_dl to collect the song and artist name from the youtube url
            video = youtube_dl.YoutubeDL({}).extract_info(youtube_url, download=False)

            song_name = video["track"]
            artist = video["artist"]

            # save the Youtube url, song name, and song artist
            self.all_song_info[video_title]={
                "youtube_url": youtube_url,
                "song_name": song_name,
                "artist": artist,

                # add the uri by calling the get_spotify_uri method so that it is easy to put the song into the playlist
                "spotify_uri":self.get_spotify_uri(song_name,artist)
            }

    # Step 3: Create a new playlist
    def create_playlist(self):
        """
        This method creates a playlist in our Spotify account.
        :return: playlist ID, the ID of the playlist
        """
        # this request body has been filled out based on the spotify web API documentation
        request_body = json.dumps({

            "name":"Liked Videos on Youtube",
            "description":"All Liked Youtube Videos",
            "public": True
        })

        # specify endpoint
        query = "https://api.spotify.com/v1/users/<MY USER ID>/playlists".format()
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type":"application.json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # make sure to save the playlist ID
        return response_json["id"]

    # Step 4: Search for the song using Spotify web API
    def get_spotify_uri(self, song_name, artist):
        """
        This method uses the spotify API in order to get the URI for each song, given the song name and artist
        :param song_name: name of the song
        :param artist: name of the artist
        :return: uri, the spotify uri for the track
        """

        # format query string to take the song and artist
        query = "https://api.spotify.com/v1/search?q={a1}%2C{s1}&type=artist%2Ctrack&market=US&limit=10&offset=5".format(
            a1 = artist,
            s1 = song_name
        )

        # send info using requests library
        response = requests.get(
            query,
            headers={
                "Content-Type": "application.json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )
        response_json = response.json()
        # we need to make sure that we know what specific songs to add
        songs = response_json["tracks"]["items"]

        # only collect the uri of the first song found
        uri = songs[0]["uri"]
        return uri


    # Step 5: Add this song into the new Spotify playlist
    def add_song_to_playlist(self):
        """
        This methods calls other methods, adds all the songs into the Spotify playlist.
        :return: json responses
        """
        # populate songs dictionary
        self.get_liked_videos()

        # collect all the uri, and put them in a list
        uris = []
        for song, info in self.all_song_info.items():
            uris.append(info["spotify_uri"])

        # create a new spotify playlist
        playlist_id = self.create_playlist()

        # populate new playlist with songs
        request_data = json.dumps(uris)

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

        # send over all URIs to the specified endpoint
        response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )

        # check for valid response status. Only give error if its neither success not created.
        if not (response.status_code == 200 or response.status_code == 201):
            raise ResponseException(response.status_code)

        response_json = response.json()
        return response_json

# driver code
if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.add_song_to_playlist()