#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit

    If an invalid subreddit is given, the function should return 0.
    """
    url_reddit = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url_reddit,
                                headers=headers,
                                allow_redirects=False)

        if response.status_code == 200:
            reddit_response = response.json()
            reddit_data = reddit_response.get("data")
            return reddit_data.get("subscribers")
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
