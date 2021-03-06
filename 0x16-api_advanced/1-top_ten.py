#!/usr/bin/python3
'''queries the Reddit API and returns the top ten posts a subreddit has'''
import requests


def top_ten(subreddit):
    '''top_ten - get's top ten posts of a subreddit'''
    user_agent = {"User-Agent": "somethingrandom"}
    amount = {"limit": 10}
    url = "https://www.reddit.com/r/" + subreddit + "/top.json"

    r_sub = requests.get(url, headers=user_agent, params=amount,
                         allow_redirects=False)
    try:
        r_sub = r_sub.json()
        for kid in r_sub.get("data").get("children"):
            print(kid.get("data").get("title"))
    except:
        print("None")
