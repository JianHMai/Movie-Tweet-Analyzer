import glob, os
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm

# Function to train model using SVM
def train():
    review = []
    sentiment = []

    location = "C:\\Users\\Jian\\Desktop\\Movie-Tweet-Sentiment-Analysis\\train.csv"
    with open(location, 'r',encoding='utf8') as csvfile: 
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

    # Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    features = vectorizer.fit_transform(review).toarray()

    # Implement SVM            
    print(svm.LinearSVC().fit(features,sentiment))

if __name__ == '__main__':
    train()
