import json

import numpy
from textblob import TextBlob
import credential
import tweepy

import re
from time import sleep

auth = tweepy.OAuthHandler(credential.consumer_key, credential.consumer_secret)

auth.set_access_token(credential.access_token, credential.access_token_secret)

# Using json parser to use raw data insetad tweepy modal
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# only retrive texts related to query (diregard other informations)

# get text only

# Utilities functions to be used after you have retrived the data
"""[summary]
   This function will resuls a list of statuses 
"""
def search_multiple_times(query, language, count_per_search, times = 1):
    # Initialize the search
    # Since twitter does not provide paging functionatinality
    # As its doc suggests, this function use maxId to extract
    primitiveStatus =  api.search(q=query, lang=language, count=count_per_search)['statuses']
    maxId = min(list(map(lambda x:x['id'], primitiveStatus)))
    result = primitiveStatus
    
    for i in range(1, times):
        currStatus =  api.search(q=query, lang=language, count=count_per_search, max_id=maxId)['statuses']
        result += currStatus
        maxId = min(list(map(lambda x:x['id'], currStatus)))
        sleep(5)
    return result
        
def unique(inputList):
    return list(set(inputList))

def get_texts(statuses):
    return list(map(lambda x: x['text'], statuses))

def clean_text(text):
    return re.sub('(https|http)://?.+', '', text)

def clean_text(texts):
    return list(map(clean_text, texts))

def get_users(statuses):
    return list(map(lambda x: x['user'], statuses))


def analyze_polarity(text_list):
    text_blob_list = list(
        map(lambda x: TextBlob(x).sentiment.polarity, text_list))
    return numpy.mean(text_blob_list)


def save_to_json(dict, name):
    output = json.dumps(dict)
    f = open(name, 'w')
    f.write(output)
    f.close()
    return


