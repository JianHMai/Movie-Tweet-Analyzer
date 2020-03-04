import bs4
import requests
from twitterscraper import query_tweets
import datetime as dt
import nltk
import pycountry

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
    begin_date = dt.date(2020,2,23)
    # Ending date
    end_date = dt.date(2020,3,1)
    limit = 1
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
        tc = nltk.classify.textcat.TextCat() 
        # Classify each tweet
        language = tc.guess_language(t.text)

        # If twitter is classified as English, save to the file
        if str(pycountry.languages.get(alpha_3=language).name) == "English":
            files.write(t.text + ',\n')
    files.close()

if __name__ == '__main__':
    get_recent_movies()