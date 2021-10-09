# Movie-Recommendation-System

#### Created and Tested on Windows 10 with Python 3.9

#### A web app that recommends you movies based on the movie you search as well as show you all the details of the movie that you have searched along with its trailer and reviews.

## Getting started

#### In order to start with the Movie Recommendation System, just clone this repository and download the TMDB movie dataset from kaggle from the below given link.

#### https://www.kaggle.com/tmdb/tmdb-movie-metadata

#### Extract the files in the Movie predictor folder. Now create a virtual environment with Python 3.9 and then install the packages in the requirements.txt file.

#### Now run the Preprocessing.ipynb file in the Movie predictor folder. You will get the finally processed dataset named final_data.csv and then run the Movie Recommender System.ipynb you will get two files similarity.pkl and movies_dict.pkl. Place the two files in the main folder. Now place your TMDB API key in the helper.py file in fetch_poster function and finally execute the command streamlit run app.py in your terminal working in the main directory. A web app will be hosted in your local machine and you are done.

## How to get the API key?

####  Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

## How does it work?

#### So basically, at first we preprocess the dataset and create a final dataset. It will then be used as a medium for gettimg recommendation based on the movie you choose or search. For that, we vectorize our final dataset and calculate the similarity score for each movie and display the top 9 movies likewise in our app. We have also used the imdb module to get the details like rating, story, cast, genres, runtime, year, languages and review of the movie we searched and the Youtube api to get the trailer of our movie. We have also applied web scraping to fetch the posters of the movie from the tmdb site.

#### The web app has been created using streamlit.

## Contribution

#### Once you get a better understanding of the project, you will see that a lot can be done with the project. You can work with improving the recommendation or add more of the latest movie data from different sites and work on them as well. You can also improve the interface by either adding more features in the web app or using other better web based applications like Django and Flask and many more. Pull requests for any changes are accepted. Feel free to fork this project and make your own changes too. 
