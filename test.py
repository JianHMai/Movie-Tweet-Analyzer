import csv
from nltk.corpus import stopwords 
import urllib.request as request
import codecs
import pickle

def test():
    loaded_model = pickle.load(open('model.sav', 'rb'))

    review = ""

    # List to hold data in columns
    X_test = []
    Y_test = []

    url = "https://raw.githubusercontent.com/JianHMai/Movie-Tweet-Sentiment-Analysis/master/test.csv"
    # Retrieve csv file from URL
    csvreader = csv.reader(codecs.iterdecode(request.urlopen(url),'utf-8'))
    # Skip header row
    next(csvreader)
    for row in csvreader:
        for word in row[0]:
            if word not in stopwords:
                review += review
        # Add X value to list 
        X_test.append(review)
        # Add Y to list with 1 given positive and 0 given negative
        if row[1] == 'positive':
            Y_test.append(1)
        else: Y_test.append(0)

    sklearn.cross_

if __name__ == '__main__':
    test()