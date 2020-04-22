import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import urllib.request as request
import codecs
import sklearn.metrics
import pickle
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 

# Function to train model using SVM
def get_data():
    # List to hold data in columns
    X = []
    y = []

    url = "https://raw.githubusercontent.com/JianHMai/Movie-Tweet-Sentiment-Analysis/master/dataset.csv"
    # Retrieve csv file from URL
    csvreader = csv.reader(codecs.iterdecode(request.urlopen(url),'utf-8'))
    # Skip header row
    next(csvreader)
    for row in csvreader:
        # Add review to list 
        X.append(row[0])
        # Add sentiment to list with 1 given positive and 0 given negative
        if row[1] == 'positive':
            y.append(1)
        else: y.append(0)       
    # Seperate training data with 80% and test data with 20% of dataset
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20)
    return X_train, X_test, y_train, y_test  

# Function to process tweets to remove stopwords and to stem
# def preprocess(review):
#     # Import stemmer
#     ps = PorterStemmer()
#     # Import list from NLTK library that contains stop words
#     stop_words = set(stopwords.words('english'))

#     for data in review:
#         print(data)
#         if not data in stop_words:
#             processed = ps.stem(data) + " "
#         break
#     print(processed)
#     return processed

# Used to classify and vectorize dataset with TF-IDF and SVM
def train(X_train, y_train):
    # Used to vectorize words and remove stop words
    vectorizer = TfidfVectorizer(stop_words='english')
    # Used to implement SVM     
    SVM = svm.LinearSVC()
    # Used to build a composite estimator using vectorizer and SVM 
    model = Pipeline([('vectorizer', vectorizer), ('SVM', SVM)])
    model.fit(X_train,y_train)

    # Save model 
    pickle.dump(model, open('model.sav', 'wb'))
    return model

# Used to validate model accuracy
def test(model):
    # Use X training data to predict using the model
    y_predict = model.predict(X_test)
    # Used to measure accuracy of model
    print(sklearn.metrics.classification_report(y_test, y_predict))

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = get_data()
    model = train(X_train, y_train)
    test(model)