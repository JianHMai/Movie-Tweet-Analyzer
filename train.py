import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import urllib.request as request
import codecs
import sklearn.metrics
import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 
import string
from nltk.tokenize import word_tokenize

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
        X.append(preprocess(row[0]))
        # Add sentiment to list with 1 given positive and 0 given negative
        if row[1] == 'positive':
            y.append(1)
        else: y.append(0)       
    # Seperate training data with 80% and test data with 20% of dataset
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20)
    return X_train, X_test, y_train, y_test  

# Function to process tweets to remove stopwords and to stem
def preprocess(review):
    # Initalize empty string
    processed = ""
    # Tokenize passed in review
    words = word_tokenize(review)
    # Import stemmer
    ps = PorterStemmer()
    # Import list from NLTK library that contains stop words
    stop_words = set(stopwords.words('english'))
    # Go through each word in list 
    for word in words:
        # If word is not a stop word,
        if not word in stop_words:
            # Stem the word
            processed += ps.stem(word) + " "
    # Replace all <br/> with an empty space
    processed = processed.replace('< br / >',' ')
    # Remove all punctuation
    processed = processed.translate(str.maketrans('', '', string.punctuation))
    # Remove all white space > 1
    processed = " ".join(processed.split())
    return processed

# Used to classify and vectorize dataset with TF-IDF and SVM
def train(X_train, y_train):
    # Used to vectorize words
    vectorizer = TfidfVectorizer(ngram_range=(2,2))
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