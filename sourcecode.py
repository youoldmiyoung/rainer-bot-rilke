#main source code

import random
import time
import sys
import tweepy
import os
from os import environ
from quotes import listR

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET_KEY = environ['CONSUMER_SECRET_KEY']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

def get_random_quote():
    randomQuote = random.choice(listR)
    return randomQuote
    x = random.randrange(1, 130)
    randomQuote = listR[rilke(x)]


def create_tweet():
    tweet = get_random_quote()
    return tweet


def tweet_quote():
    interval = 60*60*12

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)


    while True:
        print("getting a random quote :)")
        tweet = create_tweet()
        api.update_status(tweet)
        time.sleep(interval)


if __name__ == "__main__":
    tweet_quote()



