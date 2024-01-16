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
    response = requests.get(f"https://api.reddit.com/r/{subreddit}/about")
    reddit_response = response.json()

    reddit_data = reddit_response.get("data")

    if reddit_data:
        return reddit_data["subscribers"]
    else:
        return 0
