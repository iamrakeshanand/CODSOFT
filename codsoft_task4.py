# Recommendation system for movies for content based filtering
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample data with a more extensive dataset
data_dict = {
    'item_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E', 'Movie F', 'Movie G', 'Movie H', 'Movie I', 'Movie J'],
    'genre': ['Action|Adventure|Sci-Fi', 'Adventure|Fantasy', 'Action|Sci-Fi|Thriller', 'Comedy|Drama', 'Drama|Romance', 'Sci-Fi|Thriller', 
              'Action|Adventure', 'Adventure|Drama|Fantasy', 'Action|Thriller', 'Comedy|Romance']
}

# Creating DataFrame
df = pd.DataFrame(data_dict)

# Preprocess the genre column
df['genre'] = df['genre'].str.replace('|', ' ', regex=False)

# Initialize TF-IDF Vectorizer and fit_transform the genre column
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['genre'])

# Calculate the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get top N recommendations
def get_top_n_recommendations(title, cosine_sim, df, n=5):
    # Find the index of the movie that matches the title
    idx = df[df['title'] == title].index[0]
    
    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the scores of the n most similar movies, excluding the first one (itself)
    sim_scores = sim_scores[1:n+1]
    
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the top N most similar movies
    return df['title'].iloc[movie_indices]

# Example usage
title = 'Movie A'
top_n_recommendations = get_top_n_recommendations(title, cosine_sim, df, n=5)
print(f"Top 5 recommendations for {title}: {top_n_recommendations.tolist()}")
