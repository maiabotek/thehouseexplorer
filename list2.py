import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import os

# code from set environment variable on MacOS check for environment variable

if not os.getenv("SPOTIFYID"):
    raise RuntimeError("SPOTIFYID is not set")

if not os.getenv("SPOTIFYSECRET"):
    raise RuntimeError("SPOTIFYSECRET is not set")

client_id = os.getenv("SPOTIFYID")
client_secret = os.getenv("SPOTIFYSECRET")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_urls = [
    "https://open.spotify.com/playlist/37i9dQZF1EIfYEGlxfG5a0?si=19582ab0a2a94cf2",
    "https://open.spotify.com/playlist/37i9dQZF1EId9cZrsKjzaP?si=e17c21e899a3435b",
    "https://open.spotify.com/playlist/37i9dQZF1EIeXFgGD6NDh9?si=2ad6bae5f5f94572",
    "https://open.spotify.com/playlist/37i9dQZF1EIePtuqoXzsC3?si=3d034f8f113f4eb6",
    "https://open.spotify.com/playlist/37i9dQZF1EIdtA1IkngoSY?si=44d4de2271544806",
    "https://open.spotify.com/playlist/37i9dQZF1EIfI1FMWgkzcP?si=628a3ceae3c749af",
    "https://open.spotify.com/playlist/37i9dQZF1EIcACGtnmfS1M?si=69fdea3a8dbf4704"
]

genre_list = ["Hip Hop", "Deep", "Latin", "Techno", "Lo-Fi", "Old-School", "Pop"]
track_info_list = []

for playlist_index, playlist_url in enumerate(playlist_urls):

    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    playlist_uri = f"spotify:playlist:{playlist_id}"

    playlist = sp.playlist_tracks(playlist_uri)

    for idx, track in enumerate(playlist['items']):
        track_name = track['track']['name']
        track_artist = track['track']['artists'][0]['name']
        track_url = track['track']['external_urls']['spotify']
        track_url_parts = track_url.split('https://open.spotify.com')
        track_url_short = track_url_parts[1][1:]
        track_features = sp.audio_features(track['track']['id'])[0]
        track_danceability = track_features['danceability']

        track_info_list.append([idx+1, track_name, track_artist, track_url_short, track_danceability, genre_list[playlist_index]])

with open('spotify_tracks.csv', mode='w') as csv_file:
    columns = ['Index', 'Track-Name', 'Artist', 'URL', 'Danceability', 'Genre']
    writer = csv.writer(csv_file)
    writer.writerow(columns)
    for track_info in track_info_list:
        writer.writerow(track_info)
