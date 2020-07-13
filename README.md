# An Automated Spotify Playlist from YouTube Liked Videos
This project uses a Python script in order to take Liked videos from my YouTube account, and automatically add them to a dedicated Playlist in my Spotify Account.<img width="1000" alt="youtube videos to spotify picture" src="https://user-images.githubusercontent.com/62456147/87292535-88f54200-c533-11ea-9fef-ca3502093451.png">

## Motivation
I wanted to gain a better understanding of both Object-Oriented Programming, and how to use APIs to achieve tasks. Additionally, it was a good introduction to JSON and its use.

## Technologies
* Python 3.6
* JSON

## APIs
* [Youtube Data API v3]
* [Youtube_dl v 2020.01.24]
* [Spotify Web API]

## Setup
1) Install all necessary packages in the packages.txt file.
`pip3 install -r packages.txt`
* Add the exceptions.py file into the project directory.

2) Enable Oauth2.0 for Google, retrieve API key and download client_secret.json
* Go to the [Google Developers Platform] page and log into the Google account that is connected to the Youtube channel you wish to grab liked videos from.
* Create a new project, and navigate to the Credentials page for the project. 
<img width="1361" alt="Screen Shot 2020-07-13 at 7 30 15 PM" src="https://user-images.githubusercontent.com/62456147/87299811-4cc7de80-c53f-11ea-8db3-a32387242947.png">

* Click "Create Credentials". Select "OAuth Client ID", and then click Choose "Desktop App". After doing this, click the download button in order to download the client_secret.json
* Next, search for "Youtube Data API v3", and enable the API.
* Next, create an API key by again clicking "Create Credentials" and selecting "API Key".
* Copy the key and include it in the client_secret.json.
* Move the client_secret.json file into your directory containing the project.
<img width="553" alt="Screen Shot 2020-07-13 at 7 26 09 PM" src="https://user-images.githubusercontent.com/62456147/87299843-5e10eb00-c53f-11ea-9989-36cbc39cf352.png">

* For help, there is more information regarding this on the [Google Oauth2.0 Page]

3) Obtain Spotify Token and User ID. 
* To collect User ID, go to the [Account Overview] page after logging in. The User ID is your username.
* To collect the Oauth token, go to the [Get Oauth] page and click the "Get Token" button. 
* Select the scopes below:
<img width="582" alt="Screen Shot 2020-07-13 at 7 37 45 PM" src="https://user-images.githubusercontent.com/62456147/87300614-b7c5e500-c540-11ea-93df-ca3d1b33a6db.png">

* Include the Spotify User ID and Token file in the secrets.py file, and move this file into your directory containing the project.
<img width="360" alt="Screen Shot 2020-07-13 at 7 41 49 PM" src="https://user-images.githubusercontent.com/62456147/87300719-ee9bfb00-c540-11ea-8ab7-f1f392b67720.png">

4) Run the project
* Using the terminal, navigate to the directory of the project
* Run the project using `python3 automated_playlist.py`
* Copy paste the link that is generated into your browser
<img width="660" alt="Screen Shot 2020-07-13 at 7 46 03 PM" src="https://user-images.githubusercontent.com/62456147/87301413-20fa2800-c542-11ea-8d66-1354b0cfe76b.png">

* Choose the Google account that you have been working with to continue with the project, and grant permission to the project to view your Youtube account.
<img width="333" alt="Screen Shot 2020-07-13 at 7 46 32 PM" src="https://user-images.githubusercontent.com/62456147/87301580-6b7ba480-c542-11ea-878f-85099f212972.png">

* Copy the authorization code that is then given to you into your terminal
<img width="646" alt="Screen Shot 2020-07-13 at 7 47 07 PM" src="https://user-images.githubusercontent.com/62456147/87301662-92d27180-c542-11ea-8062-11e9128eee0a.png">

5) Done!
* The playlist of liked videos on Youtube is created!
<img width="784" alt="spotifyplaylist" src="https://user-images.githubusercontent.com/62456147/87301772-bac1d500-c542-11ea-8d5c-a3453c57fbef.png">

## Credits
This project was guided by [The Come Up].



   [Google Oauth2.0 Page]: https://developers.google.com/identity/protocols/oauth2
   [Youtube Data API v3]: <https://developers.google.com/youtube/v3>
   [Spotify Web API]: <https://developer.spotify.com/documentation/web-api/>
   [Youtube_dl v 2020.01.24]:<https://github.com/ytdl-org/youtube-dl/>
   [Google Developers Platform]:<https://console.developers.google.com/>
   [Account Overview]: <https://www.spotify.com/us/account/overview/>
   [Get Oauth]: <https://developer.spotify.com/console/post-playlists/>
   [The Come Up]: <https://www.youtube.com/watch?v=7J_qcttfnJA>
