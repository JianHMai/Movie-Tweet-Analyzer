import bs4
import requests
from twitterscraper import query_tweets
import datetime as dt
import nltk
import os
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 
import csv
import re
from textblob import TextBlob
import string
from nltk.tokenize import word_tokenize

# function to retrieve list of current playing movies
def get_recent_movies():
    # Link to scrape the data 
    url = "https://www.imdb.com/chart/boxoffice/?ref_=hm_cht_sm"
    response = requests.get(url)
    content = bs4.BeautifulSoup(response.content, "html.parser")
    # Find td class named titleColumn and store into movie
    movie = content.findAll('td',{'class','titleColumn'})
    # For each movie 
    for movie_name in movie:
        # Remove spaces and passes movie name into get_tweets
        get_tweets(str(movie_name.find("a").text).replace(" ", ""))

# function to retrieve tweets
def get_tweets(movie):
    # Starting date
    begin_date = dt.date(2020,2,14)

    # Ending date
    end_date = dt.date(2020,2,24)
    lang = 'english'
    # Hashtag to search 
    hashtag = "#" + movie

    # Filename to save 
    filename = movie + ".csv"
    # Create and save file in filename
    files = open(filename, 'w', encoding='utf8')

    # Calls twitter scraper library to look for tweets
    tweets = query_tweets(hashtag, begindate = begin_date, enddate = end_date, lang = lang)
    # Each tweet returned
    for t in tweets:
        text = t.text
        # Remove mentions and link from data
        text = re.sub(r"(?:\@|https?\://)\S+", "", text)
        # Remove media url from data
        text = re.sub(r"pic.twitter.com\S+", "", text)
        # Remove all punctuation from tweets
        text = text.translate(str.maketrans('', '', string.punctuation))

        # If tweet is classified as English, save to the file
        if TextBlob(text).detect_language() == 'en':
            files.write(preprocess(text) + ",")
    files.close()

# Function to preprocess csv file
def preprocess(tweet):
    # Tokenize tweets
    words = word_tokenize(tweet)
    tweet = ""
    # Import stemmer
    ps = PorterStemmer()
    # Import list from NLTK library that contains stop words
    stop_words = set(stopwords.words('english'))

    # Loop to go through list of words
    for word in words: 
        # Check in word is a stop word
        if not word in stop_words:
            # Calls the porter algo to stem
            tweet += ps.stem(word) + " "
    return tweet

if __name__ == '__main__':
    #get_recent_movies()
    get_tweets("1917Movie")