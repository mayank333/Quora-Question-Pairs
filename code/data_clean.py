import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import re
import pickle
import nltk

print('Loading data from csv..')
data = pd.read_csv('../input/test.csv')
print('Done.')

STOP_WORDS = nltk.corpus.stopwords.words()

def clean_sentence(val):
    "remove chars that are not letters or numbers, downcase, then remove stop words"
    regex = re.compile('([^\s\w]|_)+')
    sentence = regex.sub('', val).lower()
    #sentence = sentence.split(" ")

    #for word in list(sentence):
    #    if word in STOP_WORDS:
    #        sentence.remove(word)

    #sentence = " ".join(sentence)
    return sentence

def clean_dataframe(data):
    "drop nans, then apply 'clean_sentence' function to question1 and 2"
    data = data.dropna(how="any")

    for col in ['question1', 'question2']:
        print 'Cleaning col ' + col
        data[col] = data[col].apply(clean_sentence)

    return data

print('Cleaning data...')
cleaned_data = clean_dataframe(data)
print('Data cleaning done...')

cleaned_data.to_csv('../input/test_cleaned.csv')