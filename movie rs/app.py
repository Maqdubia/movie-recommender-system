import streamlit as st
import pickle
from helper import recommend

st.title('Movie Recommender System')

# Load movie list and similarity matrix
movies = pickle.load(open('model/movies.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Movie selection dropdown
selected_movie_name = st.selectbox(
    'Choose a movie to get recommendations:',
    movies['title'].values
)

# Recommend button
if st.button('Recommend'):
    names = recommend(selected_movie_name)
    st.subheader('Recommended Movies:')

    for name in names:
        st.text(name)
