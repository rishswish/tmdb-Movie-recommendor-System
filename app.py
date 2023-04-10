import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1de2952eb8be03162c84075d49e31b7e&language=en-US'.format(movie_id))

    data=response.json()
    return 'https://image.tmdb.org/t/p/original/'+data['poster_path']

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recom_mov=[]
    recom_mov_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recom_mov.append(movies.iloc[i[0]].title)
        recom_mov_posters.append(fetch_poster(movie_id))
    
    return recom_mov,recom_mov_posters
    


st.title('Movie Recommendor System')

movies=pd.read_csv('New_movies.csv')
movies_title=movies['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))

movie=st.selectbox('Which movie would you be like to recommend',movies_title)

if st.button('Recommend'):
    names,posters=recommend(movie)
    
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.image(posters[0])
        st.text(names[0])
    
    with col2:
        st.image(posters[1])
        st.text(names[1])

    with col3:
        st.image(posters[2])
        st.text(names[2])
    
    with col4:
        st.image(posters[3])
        st.text(names[3])

    with col5:
        st.image(posters[4])
        st.text(names[4])