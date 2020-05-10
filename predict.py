import joblib
import csv
import os
import glob

def predict(filename, name):
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
    return print(str(name).replace('.csv', ": ") + str(round(total/len(sentiment),4)))

if __name__ == '__main__':
    # Look through roots and subdirectory
    for root, dirs, files in os.walk("."):
        # Loop through filenames
        for name in files:
            # If the filename ends with .csv and not called dataset.csv
            if name.endswith(".csv") and name != ('dataset.csv'):
                # Call each csv file found
                predict(root + os.sep + name, name)