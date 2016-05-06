#!/usr/bin/env python3

# -*- coding: utf8 -*-

import tweepy


consumer_key = ""
consumer_secret = ""


access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)


def tdata():
    userid = str(input("Please input id who you want fav attack\n"))
    count = input("input number you want to fav!\n")
    return userid, count


def main():
    t = tdata()
    tl = []

    fav = api.user_timeline(id = t[0], count = t[1])

    for status in fav:
        tl.append(status.id_str)

    try:
        pool.map(api.create_favorite, tl)
    except tweepy.error.TweepError as e:
        if e.args[0][0]['code'] == 139:
            print("You have already favorited this status! \n")
        else:
            print(e.reason)
    finally:
            print("Done!")

if __name__ == "__main__":
    main()
