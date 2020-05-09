import joblib
import csv
import os
import glob

def predict(filename):
    total = 0
    # Load model
    loaded_model = joblib.load("model.sav")

    # Open CSV files
    files = csv.reader(open(filename, encoding = 'utf8'), delimiter=',')
    # Iterate through each review in CSV
    for line in files:
        # Using model to predict Tweeet positive or negative sentiment
        sentiment = loaded_model.predict(line)
    # Iterate through list containing sentiment for each review 
    for num in sentiment:
        # Collect total of the whole document
        total += num
    # Return file name and sentiment for whole document
    return print(str(filename).replace('.csv', ": ") + str((total/len(sentiment))))

if __name__ == '__main__':
    # Look for CSV files in current folder
    result = glob.glob('*.{}'.format('csv'))
    for file in result:
        # Skip dataset.csv
        if(file != 'dataset.csv'):
            # Call each file found in the folder
            predict(file)