#!/usr/bin/python3
'''queries the Reddit API and returns list of hot posts of a subreddit'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''top_ten - get's top ten posts of a subreddit'''
    user_agent = {"User-Agent": "somethingrandom"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"

    r_sub = requests.get(url, headers=user_agent, params={'after': after},
                         allow_redirects=False)
    if r_sub.status_code != 200:
        return (None)
    r_sub = r_sub.json()
    children = r_sub.get("data").get("children")

    if children is None or len(children) == 0:
        return (hot_list)

    for kid in children:
        hot_list.append(kid.get("data").get("title"))

    after = r_sub.get("data").get("after")

    if after == 'null' or after is None:
        return (hot_list)
    return (recurse(subreddit, hot_list, after))
