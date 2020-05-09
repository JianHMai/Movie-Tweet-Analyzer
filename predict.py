import joblib
import urllib.request as request
import csv

def predict():
    total = 0
    # Retrieve model from link
    #model = "https://github.com/JianHMai/Movie-Tweet-Sentiment-Analysis/blob/master/model.sav?raw=true"
    # Save it on computer
    #request.urlretrieve(model, "model.sav")
    loaded_model = joblib.load("model.sav")
    
    files = csv.reader(open('1917Movie_new.csv', encoding = 'utf8'), delimiter=',')
    # Iterate through each review in CSV
    for line in files:
        # Using model to predict Tweeet positive or negative sentiment
        sentiment = loaded_model.predict(line)
    # Iterate through list containing sentiment for each review 
    for num in sentiment:
        # Collect total of the whole document
        total += num
    # Return the document sentiment
    return (total/len(sentiment))

if __name__ == '__main__':
    print(predict())