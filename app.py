import pickle
import pandas as pd
import streamlit as st
import requests
import os
import gdown



import bz2



# 🔽 Step 2: Your existing code
def fetch_posters(movie_id):
    headers = {
        "accept": "application/json",

    }
    url = "https://api.themoviedb.org/3/movie/{}?api_key=3a9b0345d125a267a51923c378ce0769&language=en-US".format(movie_id)
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    except Exception as e:
        print(f"Failed to fetch poster for movie_id={movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_posters(movie_id))
    return recommended_movies, recommended_poster

# 🔽 Step 3: Load models
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
with bz2.BZ2File("similarity.pbz2", "rb") as f:
    similarity = pickle.load(f)

# 🔽 Step 4: Streamlit UI
st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Select the movie to recommend', movies['title'])

if st.button('Recommend'):
    name, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])
