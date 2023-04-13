import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Authenticate with Spotify API
scope = "playlist-modify-public"
client_id = '' # insert ID here
client_secret = '' #insert client secret here
redirect_uri = 'http://localhost:8888/callback'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope,redirect_uri=redirect_uri))

# Open the text file and read the songs
with open('songs.txt', 'r') as f:
    songs = f.read().splitlines()
    
# Search for each song and add it to a list of track URIs or not found list
tracks = []
not_found = []
for song in songs:
    query = song.split(" - ")
    if len(query) == 2:
        title, artist = query
        result = sp.search(q=f"track:{title} artist:{artist}", type='track', limit=1)
    else:
        result = sp.search(q=song, type='track', limit=1)
    if len(result['tracks']['items']) > 0:
        tracks.append(result['tracks']['items'][0]['uri'])
    else:
        not_found.append(song)
        
# Create a new playlist and add the tracks to it
playlist_id = '' #insert playlist ID here
sp.playlist_add_items(playlist_id, tracks)

# Save the not found list to a file
if not_found:
    with open('not_found.txt', 'w') as f:
        f.write('\n'.join(not_found))