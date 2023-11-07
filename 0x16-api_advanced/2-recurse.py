#!/usr/bin/python3
"""Defines a recurse function."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit. If no results are found for
    the given subreddit, returns None"""
    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0 (by Cipher10X)"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    return None
