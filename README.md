
## The House Music Explorer


### What This Code Does

This Flask app uses the Spotify API to scrape a house music playlists that are created by Spotify. Users can select different genres to explore 10 different songs, which refresh each time the page is reloaded.

### house2.py

This code scrapes Spotify playlists and writes them to a csv file, spotify_tracks, and a danceability score using the API. The flask app has two routes, one index page (index.html), and each corresponding genre page (genre.html), which are rendered as templates using Jinja. Each genre page extracts 10 random indeces from the corresponding playlist in the csv file, which is then displayed to the user through Spotify's embed feature and an appended scraped partial URL danceability score for the song.
