import pickle

# Load data
movies = pickle.load(open('model/movies.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

def recommend(movie):
    # Get movie index
    index = movies[movies['title'] == movie].index[0]

    # Sort similar movies
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    # Top 5 recommendations (excluding itself)
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies
