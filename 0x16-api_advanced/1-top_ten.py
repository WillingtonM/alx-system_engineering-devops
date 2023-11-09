#!/usr/bin/python3

"""
Reddit API query and prints titles of 1st 10 hot posts listed for a subreddit.
"""

from requests import get
from sys import argv


def top_ten(subreddit: str) -> None:
    """
    Module to get top 10 subreddits
    Args:
        subreddit (str) -> Subreddit to query
    Returns: Top 10 hots for subreddit
    """
    headers = {
        "User-Agent": "0x16-api_advanced:project"
    }

    reqst_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        resp_data = get(reqst_url, headers=headers,
                       allow_redirects=False).json()
        data = resp_data['data']['children']
        [print(post_data['data']['title']) for post_data in data[:10]]
    except Exception:
        print("None")


if __name__ == "__main__":
    (top_ten(argv[1]))
