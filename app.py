from streamlit_player import st_player
from youtubesearchpython import VideosSearch
from helper import *
from page_design import *

background_image()

# st.title('Movie Recommender System')
header("Movie Recommendation System")

header(" ")
header(" ")
header(" ")

header2("Select a movie")
selected_movie_name = st.selectbox('', movies['title'].values)

if st.button('Enter'):
    names, posters = recommend(selected_movie_name)
    rating, story, cast, genres, runtime, year, languages, rev = get_movie_details(names[0])

    s = ''
    genre = ''
    for i in genres:
        genre = genre + i + ", "
    genre1 = genre[:-2]
    genre1 = "Genre: " + genre1

    language = ''
    for i in languages:
        language = language + i + ", "
    language1 = language[:-2]
    language1 = "Languages: " + language1

    runtime = 'Runtime: ' + str(runtime[0]) + " minutes"
    year = "Release Date: " + str(year)

    rating = 'Rating: ' + str(rating) + '/10'
    c1 = 0
    for i in cast:
        s = s + str(i) + ", "
        c1 = c1 + 1
        if c1 == 13:
            break
    s1 = s[:-2] + "."

    to_search = names[0] + " Trailer " + s1[0]

    video_search = VideosSearch(to_search)
    s2 = video_search.result()

    url4 = "https://www.youtube.com/watch?v=" + s2['result'][0]['id']

    header(" ")
    header(" ")
    header(" ")
    header(" ")
    header(" ")
    header(" ")

    col10, col11 = st.columns(2)

    with col10:
        header5(names[0])
        st.image(posters[0])

    header3(rating)
    header3(genre1)
    header3(year)
    header3(runtime)
    header3(language1)

    header(" ")
    header(" ")
    header(" ")
    header(" ")

    main_movie_name("Cast:")
    movie_name(s1)

    header(" ")
    header(" ")
    header(" ")
    header(" ")

    main_movie_name("Storyline:")
    movie_name(story)

    header(" ")
    header(" ")
    header(" ")
    header(" ")
    header(" ")

    st_player(url4)

    header(" ")
    header(" ")
    header(" ")
    header(" ")
    header(" ")

    main_movie_name("Top Reviews:")

    header(" ")
    header(" ")

    header4(rev[0])

    header(" ")
    header(" ")
    header(" ")

    header4(rev[1])

    header(" ")
    header(" ")
    header(" ")

    header4(rev[2])

    header(" ")
    header(" ")
    header(" ")

    header4(rev[3])

    header(" ")
    header(" ")
    header(" ")

    header4(rev[4])

    header(" ")
    header(" ")
    header(" ")
    header(" ")
    header(" ")
    header(" ")
    header(" ")

    header2("Recommended for you:")

    header(" ")
    header(" ")

    col1, col2, col3 = st.columns(3)

    with col1:
        # st.text(names[1])
        movie_name(names[1])
        st.image(posters[1])

    with col2:
        # st.text(names[2])
        movie_name(names[2])
        st.image(posters[2])

    with col3:
        # st.text(names[3])
        movie_name(names[3])
        st.image(posters[3])

    col4, col5, col6 = st.columns(3)

    with col4:
        # st.text(names[4])
        movie_name(names[4])
        st.image(posters[4])

    with col5:
        # st.text(names[5])
        movie_name(names[5])
        st.image(posters[5])

    with col6:
        # st.text(names[6])
        movie_name(names[6])
        st.image(posters[6])

    col7, col8, col9 = st.columns(3)

    with col7:
        # st.text(names[7])
        movie_name(names[7])
        st.image(posters[7])

    with col8:
        # st.text(names[8])
        movie_name(names[8])
        st.image(posters[8])

    with col9:
        # st.text(names[9])
        movie_name(names[9])
        st.image(posters[9])
