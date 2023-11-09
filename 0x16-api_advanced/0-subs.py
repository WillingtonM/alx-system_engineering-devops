#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Gets and Returns number of subscribers for given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    get_req = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subscriberz = get_req.get("data", {}).get("subscribers", 0)
    return subscriberz
