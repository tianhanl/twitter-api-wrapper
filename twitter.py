import credential
import tweepy
import json


auth = tweepy.OAuthHandler(credential.consumer_key, credential.consumer_secret)

auth.set_access_token(credential.access_token, credential.access_token_secret)

# Using json parser to use raw data insetad tweepy modal
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# only retrive texts related to query (diregard other informations)

# get text only


def get_texts(statuses):
    return list(map(lambda x: x['text'], statuses))


def get_users(statuses):
    return list(map(lambda x: x['user'], statuses))
