#!/usr/bin/python3
"""Defines a top_ten function."""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0 (by Cipher10X)"}
    params = {"limit": 10}

    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts and isinstance(posts, list):
            for post in posts[:10]:
                print(post['data']['title'])
    else:
        print(None)
