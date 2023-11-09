#!/usr/bin/python3
""" Function that recursively queries Reddit API """
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """
    Function to recurcively query a subreddit
    & return hot topics for subreddit
    Args:
        subreddit (str): Subreddit to query
        hot_list (list): Does not have to be passed
        after (str): Does not have to be passed
        count (int): Does not have to be passed
    """
    global after
    headers = {'User-Agent': 'xica369'}
    reqst_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    resp_data = requests.get(reqst_url, headers=headers, allow_redirects=False,
                            params=params)

    if resp_data.status_code == 200:
        nxt = resp_data.json().get('data').get('after')
        if nxt is not None:
            after = nxt
            recurse(subreddit, hot_list)
        list_titles = resp_data.json().get('data').get('children')
        for list_title in list_titles:
            hot_list.append(list_title.get('data').get('title'))
        return hot_list
    else:
        return (None)
