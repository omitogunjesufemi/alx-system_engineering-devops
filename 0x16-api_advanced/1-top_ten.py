#!/usr/bin/python3
"""
Queries the Reddit API prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.

    If an invalid subreddit is given, print None.
    """
    url_reddit = f"https://api.reddit.com/r/{subreddit}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url_reddit,
                                headers=headers,
                                allow_redirects=False)

        if response.status_code == 200:
            reddit_response = response.json()
            reddit_data = reddit_response.get("data").get("children")
            for i in range(0, 10):
                data = reddit_data[i].get('data')
                print(data.get('title'))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
