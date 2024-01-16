#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles, and
prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, limit=10, after=None, hot_list={}):
    """
    A recursive function that queries the Reddit API parses
    the title of all hot articles, and prints a sorted count of
    given keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).

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

            for title in titles:
                title = title.get('data').get('title')
                for words in word_list:
                    words = words.lower()
                    if hot_list.get(words):
                        latest_count = title.lower().count(words.lower())
                        hot_list[words] = latest_count + hot_list.get(words)
                    else:
                        hot_list[words] = title.lower().count(words.lower())

            if reddit_response.get("data").get("after"):
                return count_words(subreddit,
                                   word_list, limit,
                                   after=reddit_response.get("data")
                                   .get("after"),
                                   hot_list=hot_list)
            else:
                cp_dict = hot_list.copy()
                for key, value in cp_dict.items():
                    if value == 0:
                        hot_list.pop(key)

                hot_list = dict(sorted(hot_list.items(),
                                       key=lambda x: x[1],
                                       reverse=True))
                print(hot_list)
        else:
            return None
    except requests.exceptions.RequestException:
        return None
