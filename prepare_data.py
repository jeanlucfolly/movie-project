import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# 1. Load the TMDB movies dataset
movie = pd.read_csv('tmdb_5000_movies.csv')

# 2. Use the movie overviews as text features
movie['overview'] = movie['overview'].fillna('')

# 3. Turn text into vectors
cv = CountVectorizer(stop_words='english')
count_matrix = cv.fit_transform(movie['overview'])

# 4. Compute cosine similarity between movies
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# 5. Keep only what your app needs
movie = movie[['title', 'id']].rename(columns={'id': 'movie_id'})

# 6. Save as pickle so Movieapp.py can load it
with open('movie_data.pkl', 'wb') as f:
    pickle.dump((movie, cosine_sim), f)

print("movie_data.pkl created successfully!")
