#!/usr/bin/python3
"""Defines a number_of_subscribers function."""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers.
     If an invalid subreddit is given,returns 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0 (by Cipher10X)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    return 0
