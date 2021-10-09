import pandas as pd
import pickle
import requests
from requests import get
from bs4 import BeautifulSoup
import imdb


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:10]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch posters from 8265bd1679663a7ea12ac168da84d2e8
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


def get_movie_details(user_input):
    url = get("https://www.google.com/search?q=" + user_input)
    soup = BeautifulSoup(url.text, 'html.parser')
    search_result = soup.select('.kCrYT a')
    for link in search_result[:1]:
        a = link.get('href')
        b = ''
        c = 0
        for i in range(7, len(str(a))):
            if c == 4:
                b = b + a[i]
            if a[i] == '/':
                c = c + 1
            if c == 5:
                break

    b = b[2:-1]

    moviesDB = imdb.IMDb()
    movie = moviesDB.get_movie(b)
    rating = movie['rating']
    plot_outline = movie['plot outline']
    casting = movie['cast']
    genres = movie['genres']
    runtime = movie['runtime']
    year = movie['year']
    languages = movie['languages']
    reviews = moviesDB.get_movie_reviews(b)

    rev = []
    rev1 = []

    for i in range(len(reviews['data']['reviews'])):
        rev.append(reviews['data']['reviews'][i]['content'][:400])

    for i in range(len(rev)):
        for j in range(len(str(rev[i])) - 1, 0, -1):
            if rev[i][j] == '.':
                break

        s2 = rev[i][:j + 1]
        rev1.append(s2)

    return rating, plot_outline, casting, genres, runtime, year, languages, rev1


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
