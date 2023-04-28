
## The House Music Explorer


### What This Code Does

This Flask app uses the Spotify API to scrape house music playlists, write them to a csv file, and allow users to discover new music. Each genre displays 10 randomized songs from a corresponding playlist (ex: pop genre displays songs from the pop house music playlist) and refreshes new songs each time the page is reloaded.

House2.py scrapes and writes the songs to spotify_tracks.csv, which is used to display the audio player and danceability score for each of the 10 songs on the page, all of which is gathered by the API. The Flask app has two routes, one index page (index.html), and each corresponding genre page (genre.html), which are rendered as templates using Jinja. Each genre page extracts random indexes from the corresponding playlist and song information in the csv file. The song audio players are then displayed to the user by embedding the song's scraped partial URL for the song.
