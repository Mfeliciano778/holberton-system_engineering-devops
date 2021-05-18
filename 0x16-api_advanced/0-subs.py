#!/usr/bin/python3
'''queries the Reddit API and returns the number of subs a subreddit has'''
import requests


def number_of_subscribers(subreddit):
    user_agent = {"User-Agent": "somethingrandom"}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"

    try:
        r_sub = requests.get(url, headers=user_agent).json()
        return (r_sub.get("data")["subscribers"])
    except:
        return (0)
