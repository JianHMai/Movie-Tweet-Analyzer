import joblib
import urllib.request as request
import csv

def predict():
    # Retrieve model from link
    #model = "https://github.com/JianHMai/Movie-Tweet-Sentiment-Analysis/blob/master/model.sav?raw=true"
    # Save it on computer
    #request.urlretrieve(model, "model.sav")
    loaded_model = joblib.load("model.sav")
    
    files = csv.reader(open('1917Movie_new.csv', encoding = 'utf8'), delimiter=',')
    for line in files:
        # Using model to predict Tweeet positive or negative sentiment
        return(loaded_model.predict(line)[0])

if __name__ == '__main__':
    print(predict())