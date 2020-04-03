import bs4
import requests
from twitterscraper import query_tweets
import datetime as dt
import nltk
import glob, os
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 
from nltk import word_tokenize
import csv
import re
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
import string

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
    end_date = dt.date(2020,2,16)
    limit = 800
    lang = 'english'
    # Hashtag to search 
    hashtag = "#" + movie

    # Filename to save 
    filename = movie + ".csv"
    # Create and save file in filename
    files = open(filename, 'w', encoding='utf8')

    # Calls twitter scraper library to look for tweets
    tweets = query_tweets(hashtag, begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
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
            files.write(text + ",")
    files.close()

# Function to preprocess csv file
def preprocess(location,name):
    # Filename to save 
    filename = name[:-4] + "_new.csv"
    # Create and save file in filename
    files = open(filename, 'w', encoding='utf8')

    # Import stemmer
    ps = PorterStemmer()
    # Import list from NLTK library that contains stop words
    stop_words = set(stopwords.words('english'))
    # Open and reads file and split it into objects
    words = open(location,encoding='utf8').read().split()

    # Loop to go through list of words
    for word in words: 
        # Check in word is a stop word
        if not word in stop_words:
            # Calls the porter algo to stem
            files.write(ps.stem(word) + " ")
    files.close()

# Function to train model using SVM
def train():
    review = []
    sentiment = []

    location = "C:\\Users\\Jian\\Desktop\\Movie-Tweet-Sentiment-Analysis\\dataset2.csv"
    with open(location, 'r') as csvfile: 
        csvreader = csv.reader(csvfile)
        # Skip header row
        next(csvreader)
        for row in csvreader:
            # Add review to list 
            review.append(row[0])
            # Add sentiment to list with 1 given positive and 0 given negative
            if row[1] == 'positive':
                sentiment.append(1)
            else: sentiment.append(0)

            # # Import stemmer
            # ps = PorterStemmer()
            # # Import list from NLTK library that contains stop words
            # stop_words = set(stopwords.words('english'))
            # # Open and reads file and split it into objects
            # words =  nltk.word_tokenize(review)

            # # Loop to go through list of words
            # for word in words: 
            #     # Check in word is a stop word
            #     if not word in stop_words:
            #         # Calls the porter algo to stem
            #         print(ps.stem(word) + " ")
    for x in sentiment:
        print(x)

    # Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorizer.fit(review)
    vectorizer.transform(review)
    print(vectorizer.transform(review).shape)
    print(vectorizer.vocabulary_)            

if __name__ == '__main__':
    #get_recent_movies()
    # Location to look for txt files
    #for file in os.listdir("C:\\Users\\Jian\\Desktop\\Movie-Tweet-Sentiment-Analysis\\"):
        #if file.endswith(".csv"):
            # Pass in file location for every CSV file found
            #preprocess(os.path.join("C:\\Users\\Jian\\Desktop\\Movie-Tweet-Sentiment-Analysis\\", file),file)
    train()