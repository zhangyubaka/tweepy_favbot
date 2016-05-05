#!/usr/bin/env python3

import tweepy

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userid = str(input("Please input id who you want fav attack\n"))
count = input("input number you want to fav!\n")

fav = api.user_timeline(id = userid, count = count)

try:
    for status in fav:
        api.create_favorite(status.id_str)
except:
    pass
