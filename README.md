# MOVIE-RECOMMENDATION
Another ML project which recommends movie based on genres, keywords ,casts

In this project I had taken a dataset of tmdb movie from Kaggle, processed the data , build the reommendation model and then finally created a web app using streamlit

In data processing various steps were involved in which removal of null values, took only the required features and then merge their description, keywords, genres and created a finally feature for recommendation which is tags.

Then recommend function is created which is based on vectorization (taking the closest vectors as to recommend) and on basis of their index ,recommendation is made

In the end I used streamlit to create its web app for local host

pynb file->for recommendation building
app.py ->for web app
