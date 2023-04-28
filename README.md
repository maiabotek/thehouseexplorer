
## The House Music Explorer


### What This Code Does

This Flask app uses the Spotify API to scrape a house music playlists that are created by Spotify. Users can select different genres to explore 10 different songs, which refresh each time the page is reloaded.

### house2.py

This code scrapes playlists with the Spotify API and writes them to a csv file, spotify_tracks. The flask app has two routes, one index page (index.html), and each corresponding genre page (genre.html), which are rendered as templates using Jinja. Each genre page extracts 10 random indexes from the corresponding playlist and song information in the csv file. The song and danceability score (which is gathered by the API) are displayed to the user by embedding the song's scraped partial URL for the song.
