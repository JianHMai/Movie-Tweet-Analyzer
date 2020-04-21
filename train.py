import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import urllib.request as request
import codecs
import pickle

# Function to train model using SVM
def train():
    # List to hold data in columns
    x = []
    y = []

    url = "https://raw.githubusercontent.com/JianHMai/Movie-Tweet-Sentiment-Analysis/master/dataset.csv"
    # Retrieve csv file from URL
    csvreader = csv.reader(codecs.iterdecode(request.urlopen(url),'utf-8'))
    # Skip header row
    next(csvreader)
    for row in csvreader:
        # Add review to list 
        x.append(row[0])
        # Add sentiment to list with 1 given positive and 0 given negative
        if row[1] == 'positive':
            y.append(1)
        else: y.append(0)

    # Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    features = vectorizer.fit_transform(x).toarray()

    # Implement Linear SVM            
    model = svm.LinearSVC().fit(features,y)
    # Save model 
    pickle.dump(model, open('model.sav', 'wb'))

if __name__ == '__main__':
    train()