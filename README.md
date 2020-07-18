# Sentiment Analysis with Tweets Relating to Movies 
Utilizes the Linear Support Vector Machine algorithm and TF-IDF algorithm to perform sentiment analysis on Tweets scraped from Twitter. 
<br/> <br/>
A list of current playing movies is scraped from IMDB.com and converted into hashtags. These hashtags are passed into the twitterscraper library to scrape all 
tweets written within the last 7 days. Punctuation, mentions, links, empty space, and stop words are removed during preprocessing. Also, tweets are stemmed using the 
Porter Stemming algorithm to enable faster processing. 
<br/> <br/>
The model is trained from a dataset on Kaggle.com using the Linear Support Vector Machine algorithm and TF-IDF algorithm. Utilizing a 20% test split, the 
model returns with a 90% accuracy. The model is then used to perform sentiment analysis on the Tweets where a number between zero and one is returned. 
(zero signifies negative opinion while one signifies positive opinion) 
<br/>

## Libraries Used
* Sklearn
  * SVM
  * TfidfVectorizer
  * Metrics
  * train_test_split
  * Pipeline
* NLTK
  * Stopwords
  * PorterStemmer 
  * word_tokenize
* BeautifulSoup
* twitterscraper
* Requests
