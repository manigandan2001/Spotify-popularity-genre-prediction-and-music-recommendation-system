import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Load the dataset
df = pd.read_parquet('/Users/apple/Downloads/0000 (1).parquet')
df.dropna(subset=['artists', 'album_name', 'track_name'], inplace=True)
df = df.drop_duplicates(subset=['track_id'], keep='first')
df['duration_min'] = df['duration_ms'] / 60000
df.drop('duration_ms', axis=1, inplace=True)

# Subset the data for faster testing (adjust size as needed)
df_subsample = df.sample(n=10000, random_state=42)  # Modify size or remove in production
df_subsample.reset_index(drop=True, inplace=True)

# Process data for recommendation
df_subsample['artist_list'] = df_subsample['artists'].str.split(';')
df_exploded = df_subsample.explode('artist_list')
artist_popularity = df_exploded.groupby('artist_list')['popularity'].mean().reset_index()
artist_popularity.columns = ['artist', 'avg_artist_popularity']
df_exploded = df_exploded.merge(artist_popularity, left_on='artist_list', right_on='artist', how='left')
track_avg_popularity = df_exploded.groupby('track_id')['avg_artist_popularity'].mean().reset_index()
track_avg_popularity.columns = ['track_id', 'track_avg_artist_popularity']
df_subsample = pd.merge(df_subsample, track_avg_popularity, on='track_id', how='left')

# Prepare features for cosine similarity
df_features = df_subsample[['popularity', 'danceability', 'energy', 'key', 'liveness', 
                            'valence', 'tempo', 'time_signature', 'duration_min', 
                            'track_avg_artist_popularity']]
df_sparse = csr_matrix(df_features)
similarity_matrix_sparse = cosine_similarity(df_sparse)

# Prepare other relevant columns
track_names = df_subsample['track_name'].reset_index(drop=True)
genres = df_subsample['track_genre'].reset_index(drop=True)
artists = df_subsample['artists'].reset_index(drop=True)

# Function to recommend tracks
def recommend(track_name, top_n=5):
    track_index = track_names[track_names == track_name].index[0]
    similar_tracks = pd.Series(similarity_matrix_sparse[track_index]).sort_values(ascending=False).iloc[1:top_n + 1]
    similar_tracks_names = track_names.iloc[similar_tracks.index]
    similar_tracks_genres = genres.iloc[similar_tracks.index]
    similar_tracks_artists = artists.iloc[similar_tracks.index]

    recommendations = pd.DataFrame({
        'Track Name': similar_tracks_names,
        'Genre': similar_tracks_genres.values,
        'Artist': similar_tracks_artists.values
    })
    return recommendations

# Streamlit UI
st.set_page_config(page_title="Music Recommendation System", layout="centered")

# Title with animation
st.markdown("""
<style>
@keyframes titleAnimation {
    0% { color: #ff4b4b; }
    50% { color: #4b7eff; }
    100% { color: #42ffb6; }
}
h1 {
    animation: titleAnimation 3s infinite;
}
</style>
<h1>🎵 Music Recommendation System 🎶</h1>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Welcome!")
st.sidebar.write("Select a song and get amazing recommendations based on similarity.")

# Dropdown with search box
track_choice = st.selectbox("Search or Select a Track:", options=track_names, help="Start typing the name of a song to filter.")

# Button to get recommendations
if st.button("Get Song Recommendation"):
    with st.spinner("Finding similar tracks... 🎧"):
        recommendations = recommend(track_choice)
    st.success("Here are your recommendations!")
    
    # Display recommendations
    st.table(recommendations)



