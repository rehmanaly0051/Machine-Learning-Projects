import streamlit as st
import pickle
import pandas as pd
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

API_KEY = 'b7d1678f9002da330d22536e820e6143'    

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    dists = similarity[idx]
    recs = sorted(enumerate(dists), key=lambda x: x[1], reverse=True)[1:6]
    titles, posters = [], []
    for i, _ in recs:
        titles.append(movies.iloc[i].title)
        posters.append(fetch_poster(movies.iloc[i].movie_id))
    return titles, posters

st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox('Select a movie', movies['title'].values)

st.markdown("""
    <style>
    .poster-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 8px;
    }
    .movie-title {
        width: 140px;
        white-space: nowrap;
        overflow: hidden;
        box-sizing: border-box;
    }
    .marquee {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 8s linear infinite;
    }
    @keyframes marquee {
        0%   { transform: translateX(0); }
        100% { transform: translateX(-100%); }
    }
    </style>
""", unsafe_allow_html=True)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"""
                <div class='poster-box'>
                  <div class='movie-title'>
                    <div class='marquee'>{names[i]}</div>
                  </div>
                  <img src="{posters[i]}" width="140" />
                </div>
            """, unsafe_allow_html=True)