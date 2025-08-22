# exercise5.py - A program that saves & loads movies and prints them out
import json

# A list of my 3 favorite movies
favorite_movies = ["Matrix", "Breaking Bad", "Superman"]

# Save the list to movies.json
with open("movies.json", "w") as f:
    json.dump(favorite_movies, f)

# Load it back
with open("movies.json", "r") as f:
    movies = json.load(f)

# Use a loop to print each movie
for movie in movies:
    print(movie)