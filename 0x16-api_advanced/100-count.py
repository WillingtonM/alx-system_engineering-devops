#!/usr/bin/python3
""" Module for function that queries Reddit API recursively."""
import re
import requests


def title_add(dictionary, hot_posts):
    """ Adds item into list """
    if len(hot_posts) == 0:
        return

    post_title = hot_posts[0]['data']['title'].split()
    for w in post_title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(w):
                dictionary[key] += 1
    hot_posts.pop(0)
    title_add(dictionary, hot_posts)


def recursiv(subreddit, dictionary, after=None):
    """ Queries Reddit API """
    user_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': user_agent
    }

    params = {'after': after}

    reqst_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    reqst_res = requests.get(reqst_url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if reqst_res.status_code != 200:
        return None

    reqst_dict = reqst_res.json()
    hot_posts = reqst_dict['data']['children']
    title_add(dictionary, hot_posts)
    after = reqst_dict['data']['after']
    if not after:
        return
    recursiv(subreddit, dictionary, after=after)


def count_words(subreddit, word_list, dictionary=None):
    """ Init function """
    if dictionary is None:
        dictionary = {}

    for w in word_list:
        w = w.lower()
        if w not in dictionary:
            dictionary[w] = 0

    recursiv(subreddit, dictionary)

    sortd_itms = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))
    for i in sortd_itms:
        if i[1] > 0:
            print("{}: {}".format(i[0], i[1]))
