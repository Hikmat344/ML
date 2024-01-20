import time
import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.title("Movies Recommender System")

movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity_file = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies_list['title'].tolist()


def recommendor(movie):
    f'here'
    # movie_index: int = movies_list[movies_list['title'] == movie].index[0]

    if movie in movies_list:
        movie_index = movies_list.index(movie)
        print(movie_index)
        distance = similarity_file[movie_index]
        recommended_movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies_list: list = []
        for j in recommended_movies:
           recommended_movies_list.append(movies_list.iloc[j[0]].title)

        return recommended_movies_list
    else:
        return ''



selected_movie = st.selectbox('Select your movie', movies_list)

button = st.button('recommend')
if button:
    recommendations = recommendor(selected_movie)
    for i in recommendations:
        st.write(i)

    success_message = st.empty()
    success_message.success('Recommended')
    time.sleep(2)
    success_message.empty()


