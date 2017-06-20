# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 21:02:34 2017

@author: Latif Masud
"""

import requests
import math
import unicodedata
from textblob import TextBlob as tb

def tf(word, blob):
    return float(blob.words.count(word)) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return float(math.log(float(len(bloblist)) / (1 + n_containing(word, bloblist))))

def tfidf(word, blob, bloblist):
    return float(tf(word, blob)) * float(idf(word, bloblist))

def clean_words (rm_words, query):
    wrds = query.lower()
    for word in rm_words:
        wrds = wrds.replace(word, "")
        
    return wrds
    
remove_words = ["harry", "potter", "ron", "weasley", "hermione", "granger", "hogwarts", ","]

potter_years = [2011, 2010, 2009, 2007, 2005, 2004,2002, 2001]
potter_summaries = []

for year in potter_years:
    r = requests.get('http://www.omdbapi.com/?apikey=ad492b8&t=harry+potter&y='+str(year)+'&plot=full')
    plot = unicodedata.normalize('NFKD',  r.json()["Plot"]).encode('ascii','ignore')
    potter_summaries.append(tb(clean_words(remove_words, plot)))
    
for i, blob in enumerate(potter_summaries):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, potter_summaries) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
