#!/usr/bin/env python3
"""
Author: Gabriel Lilly
Purpose: A bot designed to like tweets and follow users on Twitter
"""

import time
import tweepy

auth = tweepy.OAuthHandler(consumer_key,
                           consumer_secret)
auth.set_access_token(access_token,
                      access_token_secret)

api = tweepy.API(auth)
user = api.me()


# ------------------------------------------------------------------------------
def limit_handler(cursor):
    """Pauses for-loop when it hits the rate limit"""
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


SEARCH_STRING = 'python'
NUMBEROFTWEETS = 2


# ------------------------------------------------------------------------------
def like_tweets():
    """Like tweets on Twitter"""

    for tweet in tweepy.Cursor(api.search, SEARCH_STRING).items(NUMBEROFTWEETS):
        try:
            tweet.favorite()
            print('I liked that tweet')
        except tweepy.TweepError as any_error:
            print(any_error.reason)
        except StopIteration:
            break


# ------------------------------------------------------------------------------
def follow_back():
    """Follow users on Twitter"""
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if follower.name == 'Rhinohtownvet':
            follower.follow()
            break
