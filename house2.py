from flask import Flask, render_template
import csv
import random

app = Flask(__name__)

# Load the CSV file into a dictionary
with open('spotify_tracks.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    tracks = [row for row in csv_reader]

# Extract the unique genres from the tracks
genres = list(set([track['Genre'] for track in tracks]))

@app.route('/')
def index():
    return render_template('index.html', genres=genres)

@app.route('/genre/<string:genre>/')
def genre(genre):
    # Get a list of tracks for the specified genre
    genre_tracks = [track for track in tracks if track['Genre'] == genre]

    # Choose 10 random indices
    indices = random.sample(range(len(genre_tracks)), 10)

    # Get the tracks corresponding to the selected indices
    sample_tracks = [genre_tracks[i] for i in indices]

    return render_template('genre.html', genre=genre, tracks=sample_tracks)

if __name__ == '__main__':
    app.run(port=4999, debug=True)
