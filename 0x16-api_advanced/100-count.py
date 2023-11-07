#!/usr/bin/python3
"""Defines a count_words function."""
import requests


def count_words(subreddit, wordlist, after=None, counter={}):
    """Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
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
            title = post['data']['title'].lower().split()
            for word in wordlist:
                word = word.lower()
                if word in title:
                    count = title.count(word)
                    if not counter.get(word):
                        counter[word] = count
                    else:
                        counter[word] += count

        after = data['data']['after']
        if after:
            return count_words(subreddit, wordlist, after, counter)
        if len(counter) == 0:
            return
        counter = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
        for word, count in counter:
            print("{}: {}".format(word, count))
    else:
        return
