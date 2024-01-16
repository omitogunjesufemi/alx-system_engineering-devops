#!/usr/bin/python3
"""
Queries the Reddit API returns a list containing the titles of
all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, limit=10, after=None, hot_list=[]):
    """
    A function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.

    If an invalid subreddit is given, return None.
    """
    url_reddit = f"https://api.reddit.com/r/{subreddit}/hot"

    params = {
        'limit': limit,
        'after': after
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url_reddit,
                                params=params,
                                headers=headers,
                                allow_redirects=False)

        if response.status_code == 200:
            reddit_response = response.json()
            reddit_data = reddit_response.get("data").get("children")

            if reddit_data is None:
                return None

            titles = [post for post in reddit_data]
            hot_list.extend(titles)

            if reddit_response.get("data").get("after"):
                return recurse(subreddit, limit,
                               after=reddit_response.get("data").get("after"))
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
