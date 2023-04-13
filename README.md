# MusicMapper
MusicMapper is a command-line application that takes a text file containing a list of songs and creates a Spotify playlist with those songs. It uses the Spotify API to search for the songs and add them to the playlist.

## Requirements
- Python 3.7 or higher
- Spotify account
- Spotify API credentials (client ID and client secret)

## Installation
- Clone this repository to your local machine
''' git clone https://github.com/yourusername/songlist-to-spotify-playlist.git '''

- Install the required Python packages
'''pip install -r requirements.txt'''

- Create a .env file in the root directory of the project and add your Spotify API credentials
'''SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret'''

##Usage
- Create a text file with the list of songs you want to add to the playlist. MusicMapper will auto-format it to the following form:
'''Bohemian Rhapsody - Queen
Stairway to Heaven - Led Zeppelin
Sweet Child O' Mine - Guns N' Roses'''

- Run the tool using the following command:

'''python main.py --file path/to/songlist.txt --name "My Awesome Playlist"'''
--file specifies the path to the text file containing the song list.
--name specifies the name of the playlist to be created in your Spotify account.

The tool will prompt you to log in to your Spotify account (if you haven't already done so) and grant access to the application.
