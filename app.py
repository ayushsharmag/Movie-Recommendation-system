import pickle
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import requests
from PIL import Image
import base64
# main_bg='img.jpg'
# main_bg_ext='jpg'
# st.markdown(
#     f"""
#     <style>
#     .reportview-container {{
#         background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

def fetch_poster(movie_id):
    data=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8bf58cdc0554be6f60676804898d5c7d&language=en-US')
    data=data.json()
    poster_path="https://image.tmdb.org/t/p/w500/" +data['poster_path']
    return poster_path
# movies=pickle.load("C:\Users\AVI\Desktop\ML\Movie recommend\archive (14)\movie_recommend_model.pkl",'rb')
# movie_list[=movies.title
movies=pickle.load(open('movie_recommend_model.pkl','rb'))
st.title("Movie Recommendation by KING")
movie=st.selectbox("Select the movie",movies.title)
cv=CountVectorizer(max_features=5000,stop_words='english')
vector=cv.fit_transform(movies['tags']).toarray()
similarity=cosine_similarity(vector)
# @st.cache
def recommend(movie):
    index_movie=movies[movies.title==movie].index[0]
    distances=sorted(list(enumerate(similarity[index_movie])),reverse=True,key=lambda x:x[1])
    # col1,col2,col3,col4,col5=st.beta_columns(5)
    for i in distances[1:6]:
            st.header(movies.iloc[i[0]].title)
            # st.image(fetch_poster(movies.iloc[i[0]].id),width=300)
            img=Image.open(requests.get(fetch_poster(movies.iloc[i[0]].id),stream=True).raw)
            img=img.resize((550,350))
            st.image(img)
            st.write(movies.iloc[i[0]].overview)
        

if st.button("Recommend"):
    recommend(movie)
